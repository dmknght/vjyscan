import argparse


def get_user_options():
    parser = argparse.ArgumentParser(
        prog="vjyscan",
        description="CMS scan framework",
        add_help=True,
    )
    http_session_group = parser.add_argument_group("http_session", "HTTP Session Arguments")
    http_session_group.add_argument("--cookies", "Cookie", default="")
    http_session_group.add_argument("--proxy", "Proxy", default="")
    http_session_group.add_argument("--ua", "User Agent", default="Mozilla/5.0")
