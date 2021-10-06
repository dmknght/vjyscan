from vjyscan.cores import scan_session
from vjyscan.modules.enumerates.joomla import *
from vjyscan.modules.fingerprints import commons

target_url = "https://vjyscan.joomla.com/"
session = scan_session.VJScan(verbose=True, ua="Mozilla/5.0", cookie="", proxy="")

session.print_info(f"Scanning {target_url}")
resp = session.http_client.get(target_url)
cms = commons.response_analysis(session, data=resp.text)
if cms == "Joomla":
    version = handle_enumerate(session, target_url)

print("Completed")
