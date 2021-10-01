"""
Handle version cmp
1. split multiple versions from db (could be ranges or just versions) to 1 versions
2. Convert version length to same length (1.1.1 vs 2.2)
3. Do comparison
3a. Check exact match between target version and db version
3b. Check exact match between target version and db range
    - Check if target version >= min version
    - Check if target version <= max version or target version < max version
        Depends on db format
"""

import operator


def validate_versions(target_version: str, db_version: str) -> tuple:
    """
    Maybe the version could be in wrong format. Example: target version 1.2, db_version 1.2.3
    This function will convert format target_version and db_version to same range
    :param target_version: Target's version from parser. Format int_x.int_y.int_z (1.2.3, 1.1.1)
    :param db_version: Splited versions from db. Now it is single version is as same as db_version
    :return: target_version, db_version -> string but with same length
    """
    
    diff_dot = target_version.count(".") - db_version.count(".")
    # target_version: 1.1.1
    # db_version: 1.1
    if diff_dot > 0:
        for i in range(diff_dot):
            db_version += ".0"
        return target_version, db_version
    
    # target_version: 1.1
    # db_version: 1.1.1
    if diff_dot < 0:
        for i in range(0 - diff_dot):
            target_version += ".0"
        return target_version, db_version
    
    return target_version, db_version


def __do_cmp_version(cmp_operator: operator, target_version: str, db_version: str) -> bool:
    """

    :param cmp_operator: operator callback
    :param target_version:
    :param db_version:
    :return:
    """
    target_version, db_version = validate_versions(target_version, db_version)
    for target, db in zip(target_version.split("."), db_version.split(".")):
        if not cmp_operator(target, db):
            return False
    return True


def __cmp_with_db_version(target_version: str, db_version: str) -> bool:
    """
    Compare CMS's version with vulnerable versions in db. db_version have different syntax to define
    vulnerable versions, so we use operator lib to do dynamic check
    https://stackoverflow.com/a/36852350
    :param target_version: format int_x.int_y.int_z
    :param db_version: format int_x.int_y.int_z or int_x.int_y.int_z<=int_a.int_b.int_c
        or int_x.int_y.int_z<int_a.int_b.int_c
    :return: True if target_version is in the db_version range.
    """
    if "<=" in db_version:
        min_ver, max_ver = db_version.split("<=")
        # THINK: do we need quick string check because we are doing cmp >= for min version
        if target_version == min_ver or target_version == max_ver:
            return True
        if not min_ver:
            return __do_cmp_version(operator.le, target_version, max_ver)
        if __do_cmp_version(operator.ge, target_version, min_ver) and \
                __do_cmp_version(operator.le, target_version, max_ver):
            return True
        else:
            return False
    elif "<" in db_version:
        min_ver, max_ver = db_version.split("<")
        # THINK: do we need quick string check because we are doing cmp >= for min version
        if target_version == min_ver:
            return True
        if target_version == max_ver:
            return False
        if not min_ver:
            return __do_cmp_version(operator.le, target_version, max_ver)
        if __do_cmp_version(operator.ge, target_version, min_ver) and \
                __do_cmp_version(operator.le, target_version, max_ver):
            return True
        else:
            return False
    else:
        if target_version == db_version:
            return True
        return False


def joomla_cmp(target_version: str, db_versions: str) -> bool:
    """
    Original code: https://github.com/OWASP/joomscan/blob/master/core/compare.pl
    Original license: GPL-3
    Original version: 0.0.7 (release date Sep 24, 2018)
    Py version: 0.0.2, Date 30th Sep 2021
    Check if CMS version of website is in the range of vulnerable version. Each vulnerability in db
    could have multiple versions / multiple version ranges/
    :param target_version: Target's version from parser. ex: 1.2.3
    :param db_versions: Vulnerable version from DB, ex: 0.1.2<0.1.5 or 0.1.2 or 1.2.3|4.5.6
        or 1.2.3|4.5.6|7.7.7<7.8.8
    :return: bool -> True if target version is in vulnerable version group
    Example: joomla_cmp("0.2.3", "<=0.2.5")
    """

    # Each CVE could have multiple versions / multiple version ranges. We compare with single range
    # or single version first
    for db_version in db_versions.split("|"):
        if __cmp_with_db_version(target_version, db_version):
            return True
    return False
