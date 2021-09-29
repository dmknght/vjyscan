import re

def joomla_cmp_range(target_version: str, cmp_range_version: str) -> bool:
    """
    :param target_version: Target's version from parser
    :param cmp_range_version: Vulnerable version from DB, ex: 0.1.2<0.1.5
    :return: bool -> True if target version is in vulnerable version group
    """
    tversion = re.split("[.+:~-]", target_version)
    
    def cmp(tv: list, minv: list, maxv: list) -> bool:
        '''
        :param tv: Target's version from parser
        :param minv: Vulnerable min version from DB
        :param maxv: Vulnerable max version from DB
        :return: bool -> True if target version is in vulnerable version group
        '''

        for i in range(0, max(len(tv), len(minv), len(maxv))):
            if not tv[i]:
                tv.append(0)
                
            if not minv[i]:
                minv.append(0)
                
            if not maxv[i]:
                maxv.append(0)
            
            if int(tv[i]) > int(minv[i]) and int(tv[i]) < int(maxv[i]):
                return True
            
            if int(tv[i]) < int(minv[i]) or int(tv[i]) > int(maxv[i]):
                return False
            
        return False
    
    if cmp_range_version.find("=<=") != -1:
        range_version = re.split("=<=", cmp_range_version)
        min_version = re.split("[.+:~-]", range_version[0]) if range_version[0] != '' else [0, 0, 0]
        max_version = re.split("[.+:~-]", range_version[1])
        
        if range_version[0] == target_version and range_version[1] == target_version:
            return True
        
        return cmp(tversion, min_version, max_version)
        
    
    if cmp_range_version.find("<=") != -1:
        range_version = re.split("<=", cmp_range_version)
        min_version = re.split("[.+:~-]", range_version[0]) if range_version[0] != '' else [0, 0, 0]
        max_version = re.split("[.+:~-]", range_version[1])
        
        if range_version[1] == target_version:
            return True
        
        return cmp(tversion, min_version, max_version)
    
    if cmp_range_version.find("=<") != -1:
        range_version = re.split("=<", cmp_range_version)
        min_version = re.split("[.+:~-]", range_version[0]) if range_version[0] != '' else [0, 0, 0]
        max_version = re.split("[.+:~-]", range_version[1])
        
        if range_version[0] == target_version:
            return True
        
        return cmp(tversion, min_version, max_version)
    
    if cmp_range_version.find("<") != -1:
        range_version = re.split("<", cmp_range_version)
        min_version = re.split("[.+:~-]", range_version[0]) if range_version[0] != '' else [0, 0, 0]
        max_version = re.split("[.+:~-]", range_version[1])
        
        return cmp(tversion, min_version, max_version)

    return False

def joomla_cmp(target_version: str, cmp_version: str) -> bool:
    """
    Original code: https://github.com/OWASP/joomscan/blob/master/core/compare.pl
    Original license: GPL-3
    Original version: 0.0.7 (release date Sep 24, 2018)
    Py version: 0.0.1, Date 29th Sep 2021
    :param target_version: Target's version from parser
    :param cmp_version: Vulnerable version from DB, ex: 0.1.2<0.1.5 or 0.1.2
    :return: bool -> True if target version is in vulnerable version group
    Example: joomla_cmp("0.2.3", "<=0.2.5")
    """
    
    #
    cmp_version = cmp_version.replace(" ", "")
    if re.search("(=<.*)|(<=.*)|(=<=.*)|(<.*)", cmp_version):
        #(=<.*)|(<=.*)|(=<=.*) -> 0.1.2<0.1.5
        return joomla_cmp_range(target_version, cmp_version)
    
    if target_version == cmp_version:
        return True
    
    return False
