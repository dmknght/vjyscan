from vjyscan.resources import joomla
import json
from vjyscan.cores.version_cmp import *

db_path = joomla.__path__[0] + "core.jdb" if joomla.__path__[0].endswith("/") else joomla.__path__[0] + "/core.jdb"


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
