"""
Parse vuln info from drupal rest and other api URLS:
1. https://www.drupal.org/api-d7/node.json?type=sa&status=1&page=0 New since 2017
2. https://www.drupal.org/api-d7/node.json?taxonomy_forums=44&page=0
3. https://www.drupal.org/api-d7/node.json?taxonomy_forums=1852&page=0

Vuln info structure from json
dict_keys(['body',
'upload', 'taxonomy_forums', 'taxonomy_vocabulary_5', 'taxonomyextra', 'flag_project_issue_follow_user', 'nid',
'vid', 'is_new', 'type', 'title', 'language', 'url', 'edit_url', 'status', 'promote', 'sticky', 'created', 'changed',
'author', 'book_ancestors', 'comment', 'comments', 'comment_count', 'comment_count_new', 'feeds_item_guid',
'feeds_item_url', 'feed_nid', 'flag_flag_tracker_follow_user', 'flag_tracker_follower_count', 'has_new_content',
'last_comment_timestamp'])

Example
'body': { 'value': '<ul>\n<li>Advisory ID: DRUPAL-SA-2005-005</li>\n<li>Project:
flexinode</li>\n <li>Date: 2005-Oct-03</li>\n<li>Security risk: highly critical</li>\n <li>Impact: flexinode
module</li>\n<li>Exploitable from: remote </li>\n<li>Vulnerability: SQL injection and PHP execution by bypassing
input format check</li>\n</ul>\n <!--break--><h2>Description</h2>\n<p>Wolfgang Ziegler has discovered multiple
security vulnerabilities in the contributed <a href="http://drupal.org/project/flexinode" rel="nofollow">flexinode
module</a>.</p>\n<h2>Versions affected</h2>\n<p>Please check the CVS $Id$ fields in the following files to determine
whether the version of the flexinode module you are running is vulnerable.</p>\n<p>All versions older than the
following are vulnerable:</p>\n<h3>4.5 branch:</h3>\n<ul>\n<li>field_checkbox.inc:// $Id: field_checkbox.inc,
v 1.7.2.1 2005/09/23 01:55:07 killes Exp $</li>\n<li>field_select.inc:// $Id: field_select.inc,v 1.9.2.1 2005/09/23
01:55:07 killes Exp $</li>\n<li>field_textarea.inc:// $Id: field_textarea.inc,v 1.8.2.3 2005/09/23 02:03:02 killes
Exp $</li>\n</ul>\n<h3>4.6 branch:</h3>\n<ul>\n<li>field_checkbox.inc:// $Id: field_checkbox.inc ,v 1.7.4.1
2005/09/22 21:28:40 chx Exp $</li>\n<li>field_select.inc:// $Id: field_select.inc,v 1.9.4.1 2005/09/22 21:28:40 chx
Exp $</li>\n<li>field_textarea.inc:// $Id: field_textarea.inc,v 1.10.2.2 2005/09/22 19:37:56 chx Exp
$</li>\n</ul>\n<h3>HEAD branch:</h3>\n<ul>\n<li>field_checkbox.inc:// $Id: field_checkbox.inc,v 1.8 2005/09/23
04:28:06 chx Exp $</li>\n<li>field_select.inc:// $Id: field_select.inc,v 1.10 2005/09/23 04:28:06 chx Exp
$</li>\n<li>field_textarea.inc:// $Id: field_textarea.inc,v 1.12 2005/09/23 04:28:06 chx Exp
$</li>\n</ul>\n<h2>Solution</h2>\n<p>Drupal core is not affected. If you do not use the flexinode module there is
nothing you need to do.  If you do use flexinode, upgrade to the latest version of the flexinode module for your
Drupal version:</p>\n<ul>\n<li><a href="http://drupal.org/files/projects/flexinode-4.5.0.tar.gz" rel="nofollow">4.5
branch</a></li>\n<li><a href="http://drupal.org/files/projects/flexinode-4.6.0.tar.gz" rel="nofollow">4.6
branch</a></li>\n<li><a href="http://drupal.org/files/projects/flexinode-cvs.tar.gz" rel="nofollow">HEAD
branch</a></li>\n</ul>\n<h2>Contact</h2>\n<p>The security contact for Drupal can be reached at <a
href="mailto:security@drupal.org" rel="nofollow">security@drupal.org</a> or using the form at <a
href="http://drupal.org/contact" rel="nofollow">http://drupal.org/contact</a>.</p>', 'summary': '', 'format': '1' },
'upload': [], 'taxonomy_forums': { 'uri': 'https://www.drupal.org/api-d7/taxonomy_term/44', 'id': '44', 'resource':
'taxonomy_term' }, 'taxonomy_vocabulary_5': [], 'taxonomyextra': [], 'flag_project_issue_follow_user': [],
'nid': '32940', 'vid': '32991', 'is_new': False, 'type': 'forum', 'title': 'SQL injection and PHP code execution',
'language': 'und', 'url': 'https://www.drupal.org/forum/newsletters/security-advisories-for-contributed-projects/2005
-10-03/sql-injection-and-php-code', 'edit_url': 'https://www.drupal.org/node/32940/edit', 'status': '1', 'promote':
'0', 'sticky': '0', 'created': '1128363538', 'changed': '1169833966', 'author': { 'uri':
'https://www.drupal.org/api-d7/user/9446', 'id': '9446', 'resource': 'user', 'name': 'chx' }, 'book_ancestors': [],
'comment': '0', 'comments': [{ 'uri': 'https://www.drupal.org/api-d7/comment/58363', 'id': 58363, 'resource':
'comment' }, { 'uri': 'https://www.drupal.org/api-d7/comment/58637', 'id': 58637, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58740', 'id': 58740, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58717', 'id': 58717, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58923', 'id': 58923, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58928', 'id': 58928, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58930', 'id': 58930, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58931', 'id': 58931, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58935', 'id': 58935, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/58951', 'id': 58951, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/59090', 'id': 59090, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/59179', 'id': 59179, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/59289', 'id': 59289, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/59391', 'id': 59391, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/60480', 'id': 60480, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/60483', 'id': 60483, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/64787', 'id': 64787, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/64790', 'id': 64790, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/66697', 'id': 66697, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/68467', 'id': 68467, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/68493', 'id': 68493, 'resource': 'comment' },
{ 'uri': 'https://www.drupal.org/api-d7/comment/87049', 'id': 87049, 'resource': 'comment' }], 'comment_count': 0,
'comment_count_new': False, 'feeds_item_guid': None, 'feeds_item_url': None, 'feed_nid': None,
'flag_flag_tracker_follow_user': [], 'flag_tracker_follower_count': None, 'has_new_content': None,
'last_comment_timestamp': '1128363538' } """
import json
import requests


def parse_json_from_api(api_url: str):
    """
    Create a do_while loop to connect to each pages
    Workflow:
    1. Connect to first page
    2. Get all vuln info (to later)
    3. Get next page
    4. Go to next page or return if current page is last page
    :param api_url:
    :return:
    """
    url = api_url
    while True:
        print(f"Parsing {url}")
        resp = requests.get(url)
        data = json.loads(resp.text)
        for value in (data["list"]):
            vuln_info = value["body"]["value"]

        # When we are at last page, likely the entry next is not there
        if "next" not in data.keys():
            return

        if url == data["next"] or url == data["last"]:
            return
        else:
            url = data["next"]
        url = url.replace("node?", "node.json?")


def parse_node_sa():
    url = "https://www.drupal.org/api-d7/node.json?type=sa&status=1&page=0"
    parse_json_from_api(url)


def parse_node_44():
    url = "https://www.drupal.org/api-d7/node.json?taxonomy_forums=44&page=0"
    parse_json_from_api(url)


def parse_node_1852():
    url = "https://www.drupal.org/api-d7/node.json?taxonomy_forums=1852&page=0"
    parse_json_from_api(url)
