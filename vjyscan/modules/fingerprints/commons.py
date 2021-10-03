"""
Do common fingerprinting check
"""
import json
from vjyscan import resources

FINGERPRINT_DB = resources.__path__[0] + "/fingerprint.jdb"


def response_analysis(client, data: str) -> str:
    """
    Do first fingerprinting by check keywords are in response's text
    :param data: response's html
    :param client: session object to call print callback
    :return: name of CMS or Empty string
    """
    # Parse database
    for line in open(FINGERPRINT_DB):
        # Convert line of database to json format
        cms_fingerprint = json.loads(line)
        # Keywords is a list of keywords for CMS detection
        for keyword in cms_fingerprint["keywords"]:
            # If keywords is found, we do other CMS's analysis from response and return CMS's name
            if keyword in data:
                client.print_verbose(f"Found CMS {cms_fingerprint['name']} by keyword \"{keyword}\"")
                client.print_found(f"Found CMS {cms_fingerprint['name']}")
                # cms_fingerprint["modules"] is dictionary of name and list of keywords
                for finger_print_module in cms_fingerprint["modules"]:
                    for key, value in finger_print_module.values():
                        if value in data:
                            client.print_found(f"Found {key} by keyword {value}")
                            client.print_found(f"Found {key}")
                            # Don't run check again if the module is found
                            break
                return cms_fingerprint['name']

    return ''


def header_analysis():
    """
    Analysis's target response headers and show information
    :return:
    """
    pass
