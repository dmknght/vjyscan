import requests
import re


# Home Page: https://developer.joomla.org/security-centre.html

def __parse_part(html):
    """
    This function will parse each part of items and return list of part
    E.g:  <div ... > (get all value here) <!-- end item -->
    :param html: HTML which we get from request
    :return parts: List of item we got from parsed
    """
    html = html.replace('\t', ' '). \
        replace('\n', ' '). \
        replace('\r', ' '). \
        replace('\xa0', ''). \
        replace('</a>', '')
    html = re.sub('[ ]{2,}|<a.+?>', ' ', html)
    parts = re.findall(r'<div class="item column-1" itemprop="blogPost" itemscope itemtype='
                       r'"https://schema.org/BlogPosting">(.+?)<!-- end item -->', html)
    return parts


def __clean_unwanted_data(part):
    """
    This function will clean unwanted data from part might cause of error
        remove: <strong>, </strong>
        replace: " - Core - " to " - ", " Core " to " - "
    :param part: The string part of item before parsing
    :return part: The string after parsed
    """
    part = part.replace('<strong>', ''). \
        replace('</strong>', ''). \
        replace(' - Core - ', ' - '). \
        replace(' Core ', ' - ')
    return part


def __replace_others(version: str):
    """
    This function used when after checked and parsed the version
        will remove the unwanted characters
    :param version (string):
    :return version (string):
    """
    version = version.replace('..', '.').\
        replace(', ', '|').\
        replace('. ', '|').\
        replace('; ', '|').\
        replace(' and ', '|').\
        replace('versions', '').\
        replace('version', '').\
        replace('releases', '').\
        replace('release', '').\
        replace('x', '').\
        replace(' ', '')
    return version


def __check_version_earlier(version: str):
    """
    Just Checking for version with earlier argument
    :param version (string):
    :return:
    """
    try:
        if 'and all earlier versions' in version or bool(re.match(r'[\d.]+ and earlier$', version)):
            parse_version = re.search(r'([\d.]+) and[al ]{0,4} earlier[ version]{0,9}', version)
            string = re.sub(r'[\d.]+ and[al ]{0,4} earlier[ version]{0,9}', parse_version.group(1), version)
        else:
            parse_version = re.search(r'([\d.]+) and[al ]{0,4} earlier ([\d.]+)', version)
            if len(parse_version.group(2)) == 2:
                check_len = parse_version.group(2).replace('.', '.0')
            else:
                check_len = parse_version.group(2)
            string = re.sub(r'[\d.]+ and[al ]{0,4} earlier [\d.]+',
                            f"{check_len}.0<= {parse_version.group(1)}", version)
            string = __replace_others(string)
        version = string
    except:
        print(f'[-] Could not parse: "{version}"')
    finally:
        return version


def __version_checker(version: str):
    """
    This Function used to check the format and reformat if not match
        with our database:
        1. argument1 and all earlier argument2 => argument2<=argument1
            E.g: 2.5.13 and all earlier 2.5.x versions => 2.5.x<=2.5.13
        2. argument1 and all previous argument2 => argument2 <= argument1
            E.g:  2.5.13 and all previous 2.5.x versions => 2.5.x<=2.5.13
        3. argument1 and all argument2 => argument1 | argument2
            E.g: 1.8.0 and all 1.6.x versions => 1.8.0|1.6.x (Note: all will replace to x)
        4. argument1 and argument2 => argument1 | argument2
            E.g: 2.5.13 and 2.5.x versions => 2.5.x|2.5.13
    :param version (string): Input the version to check
    :return version (string): Output after checked
    """
    version = re.sub('<.+?>', '', version)
    if 'earlier' in version:
        version = __check_version_earlier(version)
    elif 'previous' in version:
        try:
            parse_version = re.search(r'([\d.]+) and all previous ([\d.]+) releases', version)
            version = re.sub(r'[\d.]+ and all previous [\d.]+ releases', 
                             f'{parse_version.group(2)}<={parse_version.group(1)}', version)
            version = __replace_others(version)
        except:
            print(f'[-] Could not parse: "{version}"')
    else:
        version = version.replace(', ', '|').\
            replace('. ', '|').\
            replace('; ', '|'). \
            replace('and all', '|'). \
            replace('and', '|'). \
            replace('versions', '').\
            replace('version', '').\
            replace('releases', '').\
            replace('||', '|').\
            replace(' ', '')
    version = re.sub(r'\.$', '', version)
    return version


def __parse_to_database(part):
    """
    This parser will get name of vulnerability, CVE Number, and version
        from the part which data is inputted
    :param part: The part inputted from list of parts
    :return string: {"Name": parsed_name, "CVE": CVE-Number, "version": version}
    """
    argument_error = False
    part = __clean_unwanted_data(part)
    name = re.search(r'\[[0-9]{8}][- ]{3}(.+?)[ ]{0,}</h2>', part).group(1)
    if "<li>CVE Number:" not in part:
        cve = ''
    else:
        cve = re.search(r'<li>CVE Number:(.+?)</li>', part).group(1)
    cve = cve.replace('requested', '').\
        replace(' and ', '|').\
        replace('None', '').\
        replace('Pending', '').\
        replace('Requested', '').\
        replace(' ', '')
    if 'X' in cve:
        argument_error = True
        print('[-] CVE Number problem: ', end='')
    try:
        version = re.search(r'<li>Versions:(.+?)</li>', part).group(1). \
            replace('through', '<='). \
            replace('-', '<='). \
            replace(' <= ', '<=')
        version = re.sub(r'^[ ]{0,}', '', version)
        version = __version_checker(version)
    except:  # If version not found, will continue to work and print the data
        version = ""
        argument_error = True
        print('[-] Version not found: ', end='')
    if argument_error:
        print('{' + f'"name": "{name}", "CVE": "{cve}", "version": "{version}"' + '}')
    return '{' + f'"name": "{name}", "CVE": "{cve}", "version": "{version}"' + '}'


def __get_end_page(html):
    """
    Home Page: https://developer.joomla.org/security-centre.html
    This function will get all the page that joomla homepage have
    These page will start from homepage and then add ?start=10 and
        add 10 each page
    :param html (string): The source page
    :return end_page (integer): The number of last page
    """
    end_page = 0
    try:
        end_page = re.search(r'a href="/security-centre.html\?start=(\d+?)" class="pagenav '
                             r'hasTooltip" title="End"', html).group(1)
    except:
        exit('[-] Could not get the end of page. Need to improve the code')
    finally:
        end_page = int(int(end_page) / 10 + 1)
        return end_page


def __get_html(url):
    """
    Getting text source page from url
    :param url (string): Link of homepage of core vulnerability
    :return source (string): HTML of web page
    """
    source = requests.get(url).text
    return source


def __write_to_db(list_database):
    """
    This function will check if file doesn't exist, it will make a file
        named: core.jdb and then append value to text file
    :param list_database (list): final data to output to file
    :return exit:
    """
    from os.path import isfile, isdir
    from os import makedirs

    if not isdir("../resources/joomla/"):
        makedirs("../resources/joomla/")
    if not isfile('../resources/joomla/core.jdb'):
        open('../resources/joomla/core.jdb', 'w').close()
    with open('../resources/joomla/core.jdb', 'a') as file:
        exist_data = open('../resources/joomla/core.jdb', 'r').read()
        for data in list_database:
            if data not in exist_data:
                file.write(data + '\n')
    print('[+] Updated Successfully!')


def __get_vulnerabilities(html, list_database):
    """
    This function will parse the vulnerability like Name, CVE, Version
    :param html (string): the source page
    :return: Continue of the code
    """
    parts = __parse_part(html)
    for part in parts:
        list_database.append(__parse_to_database(part))


def update_core():
    """
    This is the main of code, which will be called and returned
        the data to file: ../resources/joomla/core.jdb
    """
    list_database = []
    end_page = 0
    counter = 0
    
    while True:
        source = __get_html(f"https://developer.joomla.org/security-centre.html?start={counter * 10}")
        if end_page == 0:
            end_page = __get_end_page(source)
        __get_vulnerabilities(source, list_database)
        counter += 1
        if counter > end_page:
            break
    __write_to_db(list_database)

    from sys import exit
    exit(0)
