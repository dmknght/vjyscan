"""
Do common fingerprinting check
"""


def do_finger(client, target: str):
    resp = client.http_client.get(target)
    cms_sigs = {
        "Joomla": {
            "name": "!Joomla",
            "Debug mode": ["Joomla! Debug Console", "xdebug.org/docs/all_settings"]
        }
    }
    for key, value in cms_sigs.items():
        if value["name"] in resp.text:
            client.print_found(f"CMS: {key}")
            for fing_key, fing_value in cms_sigs[key]:
                if fing_key == "name":
                    pass
                else:
                    for each_fing_value in fing_value:
                        if each_fing_value in resp.text:
                            client.print_found(fing_key)
                            break
            return key
