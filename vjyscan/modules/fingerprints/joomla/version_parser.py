from vjyscan.cores import *
"""
Detect Joomla version
Original source: https://github.com/OWASP/joomscan/blob/master/core/ver.pl
Original License: GPL-3
Original Version: 0.0.7, Date Sep 24, 2018
Py version: 0.0.1, Date 29th Sep 2021
"""


def check_xml(client, url):
    """
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
            client.print_verbose(check_url)
        version = parse_regex(req.text, r"<version>(.*?)\<\/version>")
        if version:
            client.print_found(f"Found version {version}")
            return version
