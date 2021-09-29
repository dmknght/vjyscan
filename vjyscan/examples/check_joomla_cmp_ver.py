from vjyscan.cores.version_cmp import *
from vjyscan.cli.prints import *
from vjyscan.resources import joomla
import json

db_path = joomla.__path__[0] + "core.jdb" if joomla.__path__[0].endswith("/") else joomla.__path__[0] + "/core.jdb"

assert joomla_cmp("0.2.3", "0.2.3") == True, "OK"
assert joomla_cmp("2.3.7", "2.0.0<=2.5.7") == True, "OK"
assert joomla_cmp("2.3.5", "1.1.1<=1.1.3") == False, "OK"

for line in open(db_path):
    vuln_info = json.loads(line)
    if joomla_cmp("3.3.22", vuln_info["version"]):
        print_vulnerable(f"{vuln_info['CVE']} {vuln_info['name']}")
