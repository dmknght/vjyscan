"""
Parse vuln info from drupal rest and other api
URLS:
1. https://www.drupal.org/api-d7/node.json?type=sa&status=1&page=0 New since 2017
2. https://www.drupal.org/api-d7/node.json?taxonomy_forums=44&page=0
3. https://www.drupal.org/api-d7/node.json?taxonomy_forums=1852
"""
import json
import requests


def parse_node_sa():
    url = "https://www.drupal.org/api-d7/node.json?type=sa&status=1&page=0"
    while True:
        print(f"Parsing {url}")
        resp = requests.get(url)
        data = json.loads(resp.text)

        if url == data["next"] or url == data["last"]:
            return
        else:
            url = data["next"]
        url = url.replace("node?", "node.json?")


def parse_node_44():
    url = "https://www.drupal.org/api-d7/node.json?taxonomy_forums=44&page=0"
    while True:
        print(f"Parsing {url}")
        resp = requests.get(url)
        data = json.loads(resp.text)

        if url == data["next"] or url == data["last"]:
            return
        else:
            url = data["next"]
        if "api-d7/node?" in url:
            url = url.replace("node?", "node.json?")


parse_node_sa()
