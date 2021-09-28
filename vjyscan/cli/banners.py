def help_banner(program):
    print(f"{program} <target> [--verbose / --silent]")


def full_help_banner(program):
    help_banner(program)
    print("")
    print("  --cookie  Cookie's value")
    print("  --ua  User-Agent")
    print("  --proxy  Custom proxy address")


def program_banner(description, version, orig_name, gitlab_url):
    # from vbyscan import cores
    print("      ___      ___               ")
    print(f" __ _| _ )_  _/ __| __ __ _ _ _      ---[ \033[95m{description}\033[0m ]---")
    print(f" \\ V / _ \\ || \\__ \\/ _/ _` | ' \\     ---[  Version: \033[97m{version}\033[0m   ]---")
    print("  \\_/|___/\\_, |___/\\__\\__,_|_||_|    ---[  License: \033[93mGPL-3\033[0m   ]---")
    print("          |__/ ")
    print(f" A fork of    \033[97m{orig_name}\033[0m")
    print("")
    print("-----[ Author: \033[96mNông Hoàng Tú\033[0m ]---[ \033[37mdmknght@parrotsec.org\033[0m ]")
    print("-----[ Contributor: \033[96mLý Tuấn Kiệt\033[0m ]---[ \033[37m7heknight\033[0m ]")
    print(f"-----[ \033[94m{gitlab_url}\033[0m ]")
    print("")
