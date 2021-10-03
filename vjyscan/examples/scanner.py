from vjyscan.cores import http_session
from vjyscan.modules.enumerates.joomla import version_parser, vuln_check
from vjyscan.modules.fingerprints import commons

target_url = "https://vjyscan.joomla.com/"
session = http_session.VJScan(verbose=True, ua="Mozilla/5.0", cookie="", proxy="")

resp = session.http_client.get(target_url)
cms = commons.response_analysis(session, data=resp.text)
if cms == "Joomla":
    version = version_parser.check_xml(session, target_url)
    if version:
        vuln_check.check_core_vulns(session, version)

print("Completed")
