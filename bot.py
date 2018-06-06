import re

import irc3
import requests
from requests.compat import urljoin

issue_pattern = re.compile(r"(?:^|\s)#(\d+)", re.MULTILINE)
issue_baseurl = 'https://open-mesh.org/issues/'


@irc3.plugin
class GithubIssues:
    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.PRIVMSG)
    def has_issue(self, target, data, **kwargs):
        issues = set(issue_pattern.findall(data))
        for issue_id in issues:
            response = requests.get(urljoin(issue_baseurl, '{}.json'.format(issue_id)))

            if response.status_code == 404:
                continue

            blob = response.json()
            issue = blob['issue']

            self.bot.privmsg(
                target,
                "[{project[name]}/{id}] {subject} (by {author[name]}) -- {url}".format(
                    **issue, url=urljoin(issue_baseurl, issue_id)
                )
            )


def main():
    config = dict(
        nick='batman_issues',
        host='irc.freenode.net', port='6697', ssl='True', ssl_verify='CERT_NONE',
        max_lag=240,
        autojoins=['#batman'],
        includes=[
            'irc3.plugins.core',
            __name__,
        ]
    )

    bot = irc3.IrcBot.from_config(config)
    bot.run(forever=True)


if __name__ == '__main__':
    main()
