from vjyscan.resources import joomla
import json
from vjyscan.cores.version_cmp import *
from vjyscan.cores import *


db_path = joomla.__path__[0] + "core.jdb" if joomla.__path__[0].endswith("/") else joomla.__path__[0] + "/core.jdb"

"""
Do enumerate for Joomla CMS
"""


def check_core_vulns(client, version: str):
    """
        Compare version of Joomla with database
        Return number of vulnerabilities
        :param client: scan session to call print callbacks
        :param version: Target's versions
        :return:
        """
    count = 0
    for line in open(db_path):
        vuln_info = json.loads(line)
        if compare_versions(version, vuln_info["version"]):
            count += 1
            client.print_verbose(f"Found {vuln_info['name']}. Comparison: {version} vs {vuln_info['version']}")
            client.print_vulnerable(vuln_info['name'], cve=vuln_info["CVE"])

    client.print_info(f"Core vulnerabilities: {count}")


def enum_version_from_xml(client, url: str):
    """
    Detect Joomla version
    Original source: https://github.com/OWASP/joomscan/blob/master/core/ver.pl
    Original License: GPL-3
    Original Version: 0.0.7, Date Sep 24, 2018
    Py version: 0.0.1, Date 29th Sep 2021
        Parse version URLs bellow
          1. administrator/manifests/files/joomla.xml: Contains version of joomla
            <extension version="3.6" type="file" method="upgrade">
            <version>3.9.11</version>
            file paths in <files> and other information
          2. language/en-GB/en-GB.xml: Contains version of joomla <version>3.9.11</version>
          3. administrator/components/com_content/content.xml
            Contains version of joomla <version>3.0.0</version> (isn't as same as other path??)
            Some files of admin <administration>
            <files folder="admin">
          4. administrator/components/com_plugins/plugins.xml
            Contains version of joomla <version>3.0.0</version> (isn't as same as other path??)
          5. administrator/components/com_media/media.xml
            Contains version of joomla <version>3.0.0</version> (isn't as same as other path??)
            Other files of admin
          6. mambots/content/moscode.xml (404 not found on check target)
        :param client: HTML session, which is from cores.http_session
        :param url: Target URL
        :return: version of Joomla which is from regex
        """
    file_paths = ('administrator/manifests/files/joomla.xml', 'language/en-GB/en-GB.xml',
                  'administrator/components/com_content/content.xml',
                  'administrator/components/com_plugins/plugins.xml', 'administrator/components/com_media/media.xml',
                  'mambots/content/moscode.xml')
    for path in file_paths:
        check_url = url + path
        req = client.http_client.get(check_url)
        if req.status_code == 200:
            client.print_verbose(f"Joomla version found at {check_url}")
        version = parse_regex(req.text, r"<version>(.*?)\<\/version>")
        if version:
            client.print_found(f"Joomla version: {version}")
            return version


def find_error_logs(client, target: str):
    """
    Find common error logs
    Original code: https://github.com/OWASP/joomscan/blob/master/modules/errfinder.pl
    Original version: 0.0.1
    Original license: GPL-3
    :param client: HTML session, which is from cores.http_session
    :param target: Target's URL
    :return:
    """
    error_log_paths = (
        'error.log', 'error_log', 'php-scripts.log', 'php.errors', 'php5-fpm.log', 'php_errors.log', 'debug.log',
        'security.txt', '.well-known/security.txt')
    for path in error_log_paths:
        check_url = target + path
        req = client.http_client.get(check_url)
        if req.status_code == 200:
            client.print_found(f"Found error log: {check_url}")


def find_control_panel(client, target: str):
    """
    Find admin control panel path
    Original code: https://github.com/OWASP/joomscan/blob/master/modules/cpfinder.pl
    Original version: 0.0.1
    Original license: GPL-3
    :param client: HTML session, which is from cores.http_session
    :param target: target: Target's URL
    :return:
    """
    list_admin_path = (
        'administrator', 'admin', 'panel', 'webadmin', 'modir', 'manage', 'administration', 'joomla/administrator',
        'joomla/admin')
    for path in list_admin_path:
        check_url = target + path + "/"
        req = client.http_client.get(check_url)
        if req.status_code in (200, 403, 500, 501):
            client.print_found(f"Found control panel: {check_url}")


def find_config_backup(client, target: str):
    """
    Find backup of config files
    Original code: https://github.com/OWASP/joomscan/blob/master/modules/cpfinder.pl
    Original version: 0.0.1
    Original license: GPL-3
    :param client: HTML session, which is from cores.http_session
    :param target: target: Target's URL
    :return:
    """
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
        req = client.http_client.get(check_url)
        # Must do https://github.com/OWASP/joomscan/blob/master/modules/configfinder.pl#L10
        if req.status_code == 200:
            client.print_found(f"Found backup config file {check_url}")


def handle_enumerate(client, target: str):
    """
    Do handle all enumeration for Joomla CMS
    :param client: HTML session, which is from cores.http_session
    :param target: target: Target's URL
    :return:
    """
    version = enum_version_from_xml(client, target)
    if not version:
        # TODO try to work with other modules here
        pass
    if not version:
        print("Can't find Joomla version")
        return
    else:
        client.print_info("Scanning vulnerabilities of core")
        check_core_vulns(client, version)
        # TODO check all plugins and plugins vulns
    # TODO get a flag to handle other enumerate
    client.print_info("Check control panel")
    find_control_panel(client, target)
    client.print_info("Check backup configs")
    find_config_backup(client, target)
    client.print_info("Check error logs")
    find_error_logs(client, target)
