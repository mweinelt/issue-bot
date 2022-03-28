import logging
import re
from typing import List
from urllib.parse import urljoin

import aiohttp
import irc3  # type: ignore
import structlog
import typer

structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.INFO))
logger = structlog.get_logger()

issue_pattern = re.compile(r"(?:^|\s)#(\d+)", re.MULTILINE)
issue_endpoint = "https://api.github.com/repos/freifunk-gluon/gluon/issues/"

org = None
repo = None


@irc3.plugin
class GithubIssues:
    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.JOIN)
    async def join(self, channel: str, **kwargs):
        logger.info("join", channel=channel)

    @irc3.event(irc3.rfc.PRIVMSG)
    async def has_issue(self, mask: str, data: str, target: str, **kwargs) -> None:
        # bots may not react to notice events
        if kwargs["event"] == "NOTICE":
            return

        # find and deduplicate all issues in a message
        issues = set(issue_pattern.findall(data))

        # log privmsg if it contained issues
        if issues:
            logger.info("request", mask=mask, target=target, data=data, issues=issues)

        # fetch issue data
        async with aiohttp.ClientSession() as session:
            for issue_id in issues:
                async with session.get(urljoin(issue_endpoint, issue_id)) as response:
                    logger.debug("http", url=response.url, status=response.status)

                    if response.status == 404:
                        continue

                    blob = await response.json()
                    logger.debug("http", body=blob)

                    # format response
                    msg = "#{number} | {title} (by {user[login]}) -- {html_url}".format(
                        **blob
                    )

                    # post response
                    self.bot.notice(target, msg)

                    logger.info("response", msg=msg)


def main(
    organization: str = typer.Argument(
        ..., help="GitHub Organization name", envvar="GITHUB_ORG"
    ),
    repository: str = typer.Argument(
        ..., help="GitHub Repository name", envvar="GITHUB_REPO"
    ),
    nick: str = typer.Option(
        ..., help="Nickname on the IRC connection", envvar="IRC_NICK"
    ),
    host: str = typer.Option(..., help="Hostname of the IRC server", envvar="IRC_HOST"),
    channel: List[str] = typer.Option(
        ..., help="Channel to join on connect", envvar="IRC_CHANNELS"
    ),
    port: int = typer.Option(help="Port of the IRC Server", default=6697),
    tls: bool = typer.Option(default=True, help="Toggle TLS on the IRC connection"),
    debug: bool = typer.Option(default=False, help="Toggle debug logging"),
) -> None:

    if debug:
        global logger
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG)
        )
        logger = structlog.get_logger()

    global org, repo
    org = organization
    repo = repository

    config = dict(
        nick=nick,
        host=host,
        port=port,
        ssl=tls,
        ssl_verify="CERT_NONE",
        max_lag=240,
        autojoins=channel,
        includes=[
            "irc3.plugins.core",
            __name__,
        ],
    )

    bot = irc3.IrcBot.from_config(config)
    bot.run(forever=True)


def cli():
    typer.run(main)


if __name__ == "__main__":
    cli()
