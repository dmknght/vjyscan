from os.path import isfile
import requests
import re


# Home Page: https://developer.joomla.org/security-centre.html

def parse_part(html):
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
    parse_part_argument = re.compile('<div class="item column-1" itemprop="blogPost" itemscope '
                                     'itemtype="https://schema\.org/BlogPosting">(.+?)<!-- end item -->')
    parts = re.findall(parse_part_argument, html)
    return parts


def clean_unwanted_data(part):
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


def parse_to_database(part):
    """
    This parser will get name of vulnerability, CVE Number, and version
        from the part which data is inputted

    :param part: The part inputted from list of parts
    :return string: {"Name": parsed_name, "CVE": CVE-Number, "version": version}
    """
    part = clean_unwanted_data(part)
    name = re.search(r'\[[0-9]{8}][- ]{3}(.+?)[ ]{0,}</h2>', part).group(1)
    if "<li>CVE Number:" not in part:
        CVE = ''
    else:
        CVE = re.search(r'<li>CVE Number:(.+?)</li>', part).group(1)
    try:
        version = re.search(r'<li>Versions:(.+?)</li>', part).group(1). \
            replace('through', '<='). \
            replace('-', '<='). \
            replace(' <= ', '<=')
    except:  # If version not found, will continue to work and print the data
        version = ""
        print('[-] Version not found: ', end='')
        print('{' + f'"name": "{name}", "CVE": "{CVE}", "version": "{version}"' + '}\n')
    return '{' + f'"name": "{name}", "CVE": "{CVE}", "version": "{version}"' + '}'


def get_vulnerabilities(html, list_database):
    """
    This function will parse the vulnerability like Name, CVE, Version
    :param html (string): the source page
    :return: Continue of the code
    """
    parts = parse_part(html)
    for part in parts:
        list_database.append(parse_to_database(part))


def start_parsing(end_page):
    """
    This function will gain page and then start to
        parse by calling other function
        Page: https://developer.joomla.org/security-centre.html?start=number*10
    :param end_page (integer): the number of last page
    :return list_database (list): the final data
    """
    list_database = []
    for page in range(0, end_page):
        html = requests.get(f"https://developer.joomla.org/security-centre.html?start={page * 10}").text
        get_vulnerabilities(html, list_database)
    return list_database


def get_end_page(html):
    """
    Home Page: https://developer.joomla.org/security-centre.html
    This function will get all the page that joomla homepage have
    These page will start from homepage and then add ?start=10 and
        add 10 each page

    :param html (string): The source page
    :return end_page (integer): The number of last page
    """
    end_page = 0
    parse_arguments = re.compile(
        'a href="/security-centre.html\?start=(\d+?)" class="pagenav hasTooltip" title="End"')
    try:
        end_page = re.search(parse_arguments, html).group(1)
    except:
        exit('[-] Could not get the end of page. Need to improve the code')
    finally:
        end_page = int(int(end_page) / 10 + 1)
        return end_page


def get_html(url):
    """
    Getting text source page from url

    :param url (string): Link of homepage of core vulnerability
    :return source (string): HTML of web page
    """
    source = requests.get(url).text
    return source


def write_to_db(list_database):
    """
    This function will check if file doesn't exist, it will make a file
        named: core.jdb and then append value to text file

    :param list_database (list): final data to output to file
    :return exit:
    """
    if not isfile('core.jdb'):
        open('core.jdb', 'w').close()
    with open('core.jdb', 'a') as file:
        exist_data = open('core.jdb', 'r').read()
        for data in list_database:
            if data not in exist_data:
                file.write(data + '\n')
    print('[+] Updated Successfully!')
    return exit(0)


def update_core():
    """
    This is the main of code, which will be called and returned
        the data to file: ../resources/joomla/core.jdb
    """
    home_page = 'https://developer.joomla.org/security-centre.html'
    source = get_html(home_page)
    end_page = get_end_page(source)
    list_database = start_parsing(end_page)
    write_to_db(list_database)
