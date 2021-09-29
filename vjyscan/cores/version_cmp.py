

def joomla_cmp(target_version, to_cmp_version):
    """
    Original code: https://github.com/OWASP/joomscan/blob/master/core/compare.pl
    Original license: GPL-3
    Original version: 0.0.7 (release date Sep 24, 2018)
    Py version: 0.0.1, Date 29th Sep 2021
    :param target_version: Target's version from parser
    :param to_cmp_version: Vulnerable version from DB
    :return: bool -> True if target version is in vulnerable version group
    """

