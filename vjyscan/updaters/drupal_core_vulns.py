"""
Parse vuln info from drupal rest and other api
URLS:
1. https://www.drupal.org/api-d7/node.json?type=sa&status=1&page=0 New since 2017
2. https://www.drupal.org/api-d7/node.json?taxonomy_forums=44&page=0
3. https://www.drupal.org/api-d7/node.json?taxonomy_forums=1852&page=0
"""
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
