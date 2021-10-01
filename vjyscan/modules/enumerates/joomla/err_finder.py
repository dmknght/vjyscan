"""
Find common error logs
Original code: https://github.com/OWASP/joomscan/blob/master/modules/errfinder.pl
Original version: 0.0.1
Original license: GPL-3
"""


def do_check_error_logs(client, target):
    error_log_paths = (
        'error.log', 'error_log', 'php-scripts.log', 'php.errors', 'php5-fpm.log', 'php_errors.log', 'debug.log',
        'security.txt', '.well-known/security.txt')
    for path in error_log_paths:
        check_url = target + path
        req = client.http_client.get(check_url)
        if req.status_code == "200":
            client.print_found(check_url)
