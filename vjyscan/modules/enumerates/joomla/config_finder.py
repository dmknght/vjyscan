"""
Find backup of config files
Original code: https://github.com/OWASP/joomscan/blob/master/modules/cpfinder.pl
Original version: 0.0.1
Original license: GPL-3
"""


def do_config_finder(client, target: str):
    config_paths = ('configuration.php_old', 'configuration.php_new', 'configuration.php~', 'configuration.php.new',
                    'configuration.php.new~', 'configuration.php.old', 'configuration.php.old~', 'configuration.bak',
                    'configuration.php.bak', 'configuration.php.bkp', 'configuration.txt', 'configuration.php.txt',
                    'configuration - Copy.php', 'configuration.php.swo', 'configuration.php_bak', 'configuration.php#',
                    'configuration.orig', 'configuration.php.save', 'configuration.php.original',
                    'configuration.php.swp', 'configuration.save', '.configuration.php.swp', 'configuration.php1',
                    'configuration.php2', 'configuration.php3', 'configuration.php4', 'configuration.php4',
                    'configuration.php6', 'configuration.php7', 'configuration.phtml', 'configuration.php-dist')

    for path in config_paths:
        check_url = target + path
        req = client.http_client(check_url)
        # Must do https://github.com/OWASP/joomscan/blob/master/modules/configfinder.pl#L10
        if req.status_code == 200:
            client.print_found(check_url)
