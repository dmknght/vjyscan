from vjyscan.cores.version_cmp import *
from vjyscan.cli.prints import *
from vjyscan.resources import joomla
import json

db_path = joomla.__path__[0] + "core.jdb" if joomla.__path__[0].endswith("/") else joomla.__path__[0] + "/core.jdb"

# Test validate versions
assert validate_versions("0.1", "2.1.3") == ("0.1.0", "2.1.3"), "Wrong ('0.1', '2.1.3')"
assert validate_versions("0.1", "2.1.3") != ("0.1", "2.1.3"), "Wrong ('0.1', '2.1.3')"
assert validate_versions("0.1.2", "2.1") == ("0.1.2", "2.1.0"), "Wrong ('0.1.2', '2.1')"
assert validate_versions("0.1.2", "2.1") != ("0.1.2", "2.1"), "Wrong ('0.1.2', '2.1')"

# Test check joomla compare version
assert joomla_cmp("0.2.3", "0.2.3") == True, "Wrong, 0.2.3"
assert joomla_cmp("2.3.7", "2.0.0<=2.5.7") == True, "Wrong, 2.0.0<=2.5.7"
assert joomla_cmp("2.3.5", "1.1.1<=1.1.3") == False, "Wrong 1.1.1<=1.1.3"
assert joomla_cmp("2.3.5", "2.0.0<2.3.5") == False, "Wrong 2.0.0<2.3.5"
assert joomla_cmp("2.3.5", "2.0.0<=2.3.5") == True, "Wrong 2.0.0=<2.3.5"
assert joomla_cmp("2.3.5", "<=2.3.5") == True, "Wrong <=2.3.5"
assert joomla_cmp("2.3.7", "<=2.3.5") == False, "Wrong <=2.3.5"


for line in open(db_path):
    vuln_info = json.loads(line)
    if joomla_cmp("3.3.22", vuln_info["version"]):
        print_vulnerable(f"{vuln_info['CVE']} {vuln_info['name']}")
