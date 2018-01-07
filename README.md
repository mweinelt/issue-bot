# What

Bot.

# What?!

Connects to IRC, joins Channel.

Reacts on #\d+, fetches issue from GitHub, spits out the headlines

#



GitHub v3 Issue looks like this:

```
{
  "url": "https://api.github.com/repos/freifunk-gluon/gluon/issues/1284",
  "repository_url": "https://api.github.com/repos/freifunk-gluon/gluon",
  "labels_url": "https://api.github.com/repos/freifunk-gluon/gluon/issues/1284/labels{/name}",
  "comments_url": "https://api.github.com/repos/freifunk-gluon/gluon/issues/1284/comments",
  "events_url": "https://api.github.com/repos/freifunk-gluon/gluon/issues/1284/events",
  "html_url": "https://github.com/freifunk-gluon/gluon/issues/1284",
  "id": 284444756,
  "number": 1284,
  "title": "route lost on hostapd disassociate",
  "user": {
    "login": "christf",
    "id": 4321652,
    "avatar_url": "https://avatars3.githubusercontent.com/u/4321652?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/christf",
    "html_url": "https://github.com/christf",
    "followers_url": "https://api.github.com/users/christf/followers",
    "following_url": "https://api.github.com/users/christf/following{/other_user}",
    "gists_url": "https://api.github.com/users/christf/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/christf/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/christf/subscriptions",
    "organizations_url": "https://api.github.com/users/christf/orgs",
    "repos_url": "https://api.github.com/users/christf/repos",
    "events_url": "https://api.github.com/users/christf/events{/privacy}",
    "received_events_url": "https://api.github.com/users/christf/received_events",
    "type": "User",
    "site_admin": false
  },
  "labels": [
    {
      "id": 384303471,
      "url": "https://api.github.com/repos/freifunk-gluon/gluon/labels/Babel",
      "name": "Babel",
      "color": "669933",
      "default": false
    }
  ],
  "state": "open",
  "locked": false,
  "assignee": null,
  "assignees": [

  ],
  "milestone": null,
  "comments": 3,
  "created_at": "2017-12-25T12:47:26Z",
  "updated_at": "2017-12-28T11:33:56Z",
  "closed_at": null,
  "author_association": "CONTRIBUTOR",
  "body": "when a client is disconnected (see 13:31:18 hostapd message) and re-connects afterwards (see 13:31:27 hostapd message) the client is losing its default route and therefore connectivity.\r\nThis may happen on difficult wifi situations.\r\n```\r\nMon Dec 25 13:31:15 2017 kern.warn kernel: [45020.393820] REJECT(src wan)IN=br-wan OUT= MAC=ff:ff:ff:ff:ff:ff:de:42:86:62:89:92:08:00 SRC=192.168.13.117 DST=192.168.13.255 LEN=97 TOS=0x00 PREC=0x00 TTL=64 ID=28746 DF PROTO=UDP SPT=39311 DPT=21027 LEN=77 \r\nMon Dec 25 13:31:15 2017 daemon.info fastd[1863]: sending handshake to <mesh_vpn_backbone_peer_babelgw2>[185.206.209.154:10001]...\r\nMon Dec 25 13:31:15 2017 daemon.info fastd[1863]: resolving host `gw02.babel.ffffm.net' for peer <mesh_vpn_backbone_peer_babelgw2>...\r\nMon Dec 25 13:31:15 2017 daemon.info fastd[1863]: resolved host `gw02.babel.ffffm.net' successfully\r\nMon Dec 25 13:31:18 2017 daemon.info fastd[1863]: resolving host `gw04.babel.ffffm.net' for peer <mesh_vpn_backbone_peer_babelgw4>...\r\nMon Dec 25 13:31:18 2017 daemon.info fastd[1863]: resolved host `gw04.babel.ffffm.net' successfully\r\nMon Dec 25 13:31:18 2017 daemon.notice hostapd: client0: AP-STA-DISCONNECTED 60:57:18:88:d7:f9\r\nMon Dec 25 13:31:21 2017 daemon.info fastd[1863]: sending handshake to <mesh_vpn_backbone_peer_babelgw3>[[2a06:8187:fb14:1::3:1]:10001]...\r\nMon Dec 25 13:31:22 2017 daemon.notice netifd: wan (994): udhcpc: sending renew\r\nMon Dec 25 13:31:22 2017 daemon.notice netifd: wan (994): udhcpc: lease of 192.168.13.161 obtained, lease time 3600\r\nMon Dec 25 13:31:27 2017 daemon.info hostapd: client0: STA 60:57:18:88:d7:f9 IEEE 802.11: authenticated\r\nMon Dec 25 13:31:27 2017 daemon.info hostapd: client0: STA 60:57:18:88:d7:f9 IEEE 802.11: associated (aid 2)\r\nMon Dec 25 13:31:27 2017 daemon.notice hostapd: client0: AP-STA-CONNECTED 60:57:18:88:d7:f9\r\nMon Dec 25 13:31:27 2017 daemon.info hostapd: client0: STA 60:57:18:88:d7:f9 IEEE 802.11: associated (aid 2)\r\nMon Dec 25 13:31:27 2017 daemon.info hostapd: client0: STA 60:57:18:88:d7:f9 IEEE 802.11: associated (aid 2)\r\nMon Dec 25 13:31:36 2017 daemon.info fastd[1863]: sending handshake to <mesh_vpn_backbone_peer_babelgw2>[[2a06:8187:fb14:1::2:1]:10001]...\r\nMon Dec 25 13:31:37 2017 kern.warn kernel: [45042.333568] REJECT(src wan)IN=br-wan OUT= MAC=ff:ff:ff:ff:ff:ff:d0:50:99:47:70:66:08:00 SRC=192.168.13.9 DST=192.168.13.255 LEN=76 TOS=0x18 PREC=0xA0 TTL=64 ID=52536 DF PROTO=UDP SPT=123 DPT=123 LEN=56 \r\nMon Dec 25 13:31:38 2017 authpriv.info dropbear[31548]: Child connection from 2a06:8187:fbab:2:2457:abd:3f3f:ec28:45368\r\nMon Dec 25 13:31:39 2017 daemon.info fastd[1863]: sending handshake to <mesh_vpn_backbone_peer_babelgw4>[[2a06:8187:fb14:1::4:1]:10001]...\r\nMon Dec 25 13:31:42 2017 authpriv.info dropbear[30211]: Exit (root): Error writing: Connection reset by peer\r\n```",
  "closed_by": null
}
```