def dummy(*args, **kwargs):
    pass


def print_verbose(message: str, tab: int = 1):
    spaces = tab * "  "
    print(f"{spaces}- {message}")


def print_vulnerable(name, uri="", cve=""):
    # Bright Magenta
    print(f"  [\033[96m*\033[0m] \033[95m{name}\033[0m is\033[91m vulnerable\033[0m")
    if uri:
        # Bright Cyan
        print(f"  \033[96m{uri}\033[0m")
    if cve:
        print(f"  CVE ID: \033[96m{cve}\033[0m")


def print_not_vulnerable(name):
    # Bright yellow
    print(f"  [\033[93m!\033[0m] \033[93m{name}\033[0m is\033[37m not vulnerable\033[0m")


def print_found(message, uri=""):
    # Bright white
    print(f"  [\033[97m*\033[0m] \033[97m{message}\033[0m")
    if uri:
        # Bright blue
        print(f"  \033[94m{uri}\033[0m")


def print_not_found(message):
    print(f"  [\033[91m-\033[0m] {message} not found")


def print_info(message: str):
    print(f" [\033[97mINF\033[0m] \033[97m{message}\033[0m")
