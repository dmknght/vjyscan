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
    
    def cmp(tv: list, start_v: list, end_v: list) -> bool:
        """
        :param tv: Target's version from parser
        :param start_v: Vulnerable start version from DB
        :param end_v: Vulnerable end version from DB
        :return: bool -> True if target version is in vulnerable version group
        """

        for i in range(0, max(len(tv), len(start_v), len(end_v))):
            if not tv[i]:
                tv.append(0)

            if not start_v[i]:
                start_v.append(0)

            if not end_v[i]:
                end_v.append(0)

            if int(start_v[i]) < int(tv[i]) < int(end_v[i]):
                return True

            if int(tv[i]) < int(start_v[i]) or int(tv[i]) > int(end_v[i]):
                return False

        return False

    tversion = target_version.split(".")
    cmp_version = cmp_version.replace('', '')
    list_cmp_version = cmp_version.split('<')
    
    if len(list_cmp_version) >= 2:
        start_version = list_cmp_version[0] if list_cmp_version[0] != '' else '0.0.0'
        start_version = start_version if start_version != '=' else '0.0.0' + start_version
        end_version = list_cmp_version[1]
        
        #ex: 1.2.4 compare 1.2.3=<=1.2.5 -> True
        #ex: 1.2.3 compare 1.2.3=<=1.2.5 -> True
        #ex: 1.2.5 compare 1.2.3=<=1.2.5 -> True
        #ex: 1.2.2 compare 1.2.3=<=1.2.5 -> False
        #ex:  1.2.6 compare 1.2.3=<=1.2.5 -> False
        if start_version.endswith('=') and end_version.startswith('='):
            
            start_version = start_version.replace('=', '')
            end_version = end_version.replace('=', '')
            
            if start_version == target_version or end_version == target_version:
                return True
            
            start_version = start_version.split('.')
            end_version = end_version.split('.')
            
            return cmp(tversion, start_version, end_version)
        
        #ex: 1.2.3 compare 1.2.3=<1.2.5 -> True
        #ex: 1.2.5 compare 1.2.3=<1.2.5 -> False
        if start_version.endswith('='):
            start_version = start_version.replace('=', '')
            
            if start_version == target_version:
                return True
            
            start_version = start_version.split('.')
            end_version = end_version.split('.')
            
            return cmp(tversion, start_version, end_version)
        
        #ex: 1.2.3 compare 1.2.3<=1.2.5 -> False
        #ex: 1.2.5 compare 1.2.3<=1.2.5 -> True
        if end_version.startswith('='):
            
            end_version = end_version.replace('=', '')
            
            if end_version == target_version:
                return True
            
            start_version = start_version.split('.')
            end_version = end_version.split('.')
            
            return cmp(tversion, start_version, end_version)
        
    if len(list_cmp_version) == 1 and target_version == list_cmp_version[0]:
        return True
    
    return False
