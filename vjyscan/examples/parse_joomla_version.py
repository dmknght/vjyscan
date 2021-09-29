from vjyscan.cores import http_session
from vjyscan.modules.fingerprints.joomla import version_parser

session = http_session.VJScan(verbose=True, ua="Mozilla/5.0", cookie="", proxy="")

target_url = "https://ktht.nuce.edu.vn/"

print(version_parser.check_xml(session, target_url))
