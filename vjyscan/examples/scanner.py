from vjyscan.cores import scan_session
from vjyscan.modules.enumerates.joomla import version_parser, vuln_check
from vjyscan.modules.fingerprints import commons

target_url = "https://vjyscan.joomla.com/"
session = scan_session.VJScan(verbose=False, ua="Mozilla/5.0", cookie="", proxy="")

session.print_info(f"Scanning {target_url}")
resp = session.http_client.get(target_url)
cms = commons.response_analysis(session, data=resp.text)
if cms == "Joomla":
    version = version_parser.check_xml(session, target_url)
    if version:
        session.print_info("Scanning vulnerabilities of core")
        core_vulns = vuln_check.check_core_vulns(session, version)

session.print_info(f"Core vulnerabilities: {core_vulns}")
print("Completed")
