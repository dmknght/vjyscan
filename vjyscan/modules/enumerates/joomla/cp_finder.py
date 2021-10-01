"""
Find admin control panel path
Original code: https://github.com/OWASP/joomscan/blob/master/modules/cpfinder.pl
Original version: 0.0.1
Original license: GPL-3
"""


def do_admin_finder(client: any, target: str):
    list_admin_path = (
        'administrator', 'admin', 'panel', 'webadmin', 'modir', 'manage', 'administration', 'joomla/administrator',
        'joomla/admin')
    for path in list_admin_path:
        check_url = target + path + "/"
        req = client.http_client(check_url)
        if req.status_code in (200, 403, 500, 501):
            client.print_found(check_url)
