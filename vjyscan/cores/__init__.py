import re


def parse_regex(data, regex):
    try:
        result = re.findall(regex, data)[0]
        if result:
            return result
    except Exception:
        return ""
