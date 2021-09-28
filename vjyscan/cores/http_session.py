import requests
from vjyscan.cli.prints import *


class VJScan:
    def __init__(self, ua, proxy, cookie, verbose):
        self.print_vulnerable = print_vulnerable
        self.print_found = print_found
        if verbose:
            self.print_verbose = print_verbose
            self.print_not_vulnerable = print_not_vulnerable
            self.print_not_found = print_not_found
        else:
            self.print_verbose = dummy
            self.print_not_vulnerable = dummy
            self.print_not_found = dummy
        self.http_client = requests.Session()
        self.http_client.headers.update({'User-Agent': ua})
        if proxy:
            self.http_client.proxies.update({'http': proxy})  # must check https proxies
        if cookie:
            self.http_client.cookies.set_cookie(cookie)
