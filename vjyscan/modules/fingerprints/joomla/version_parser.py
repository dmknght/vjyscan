"""
Detect Joomla version
Original source: https://github.com/OWASP/joomscan/blob/master/core/ver.pl
Original License: GPL-3
Original Version: 0.0.7, Date Sep 24, 2018
Py version: 0.0.1, Date 29th Sep 2021
"""


def check_xml(client, url):
    """
    Parse version from ('administrator/manifests/files/joomla.xml','language/en-GB/en-GB.xml',
    'administrator/components/com_content/content.xml','administrator/components/com_plugins/plugins.xml',
    'administrator/components/com_media/media.xml','mambots/content/moscode.xml')
    :param client: HTML session, which is from cores.http_session
    :param url: Target URL
    :return: version of Joomla
    """
    file_paths = ('administrator/manifests/files/joomla.xml', 'language/en-GB/en-GB.xml',
                  'administrator/components/com_content/content.xml',
                  'administrator/components/com_plugins/plugins.xml', 'administrator/components/com_media/media.xml',
                  'mambots/content/moscode.xml')
    for path in file_paths:
        check_url = url + path
        req = client.http_client.get(check_url)
        print(req.text)
