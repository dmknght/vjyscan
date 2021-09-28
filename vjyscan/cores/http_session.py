import requests
from vjyscan.cli.prints import *


class VJScan:
    def __init__(self, verbose=False):
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
        # TODO add proxy, cookie, agent handler
