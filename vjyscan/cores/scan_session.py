import requests
from vjyscan.cli.prints import *


class VJScan:
    def __init__(self, ua, proxy, cookie, verbose):
        self.print_vulnerable = print_vulnerable
        self.print_found = print_found
        self.print_info = print_info
        if verbose:
            self.print_verbose = print_verbose
            self.print_not_vulnerable = print_not_vulnerable
            self.print_not_found = print_not_found
        else:
            self.print_verbose = dummy
            self.print_not_vulnerable = dummy
            self.print_not_found = dummy
        self.http_client = requests.Session()
        # README: python3-request has error urllib3.exceptions.LocationParseError: Failed to parse
        # The problem is because of module six
        # Conflict: pwntools
        # Solution: upgrade module six to version 16 (pip3 install six --upgrade)
        self.http_client.headers.update({'User-Agent': ua})
        if proxy:
            self.http_client.proxies.update({'http': proxy})  # must check https proxies
        if cookie:
            self.http_client.cookies.set_cookie(cookie)
