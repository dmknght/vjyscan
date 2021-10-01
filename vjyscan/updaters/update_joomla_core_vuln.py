# Source: https://developer.joomla.org/security-centre.html?start=120
from os.path import isfile
import requests
import re

# Static Variable
URL = 'https://developer.joomla.org/security-centre.html'


# =================== Parse Part =================== #

def parse_to_database(data):
    name = re.search(r'Core[ -]{3}(.+?) </h2>', data).group(1)
    if "CVE Number:" not in data:
        CVE = ""
    else:
        CVE = re.search(r'<li><strong>CVE Number:</strong>[ ]{0,}(.+?)[ ]{0,}</li>', data).group(1)
    version = re.search(r'<li><strong>Versions:[ ]{1,}</strong>(.+?)</li>', data).group(1)
    version = re.sub('[ -]{2,}| through ', "<=", version)
    print({"name": name, "CVE": CVE, "version": version})
    # return {"name": name, "CVE": CVE}


#  === Done ===  #
def parse_part(source):
    source = re.sub('[ \t\n\r]{1,}', ' ', source)
    source = re.sub('[ ]{2,}|<a.+?>|</a>', ' ', source)
    parse_part_argument = r'<div class="item column-1" itemprop="blogPost" itemscope itemtype="https://schema\.org/BlogPosting">(.+?)<!-- end item -->'
    part = re.findall(parse_part_argument, source)
    return part


def parsing(data, arguments):
    try:
        return re.search(arguments, data).group(0)
    except:
        return ""


# =================== GET LINK =================== #

#  === Done ===  #
def get_html(url):
    text = requests.get(url).text
    return text


def get_page_links(data):
    list_link = []
    list_link.append(URL)
    end_page = 0
    try:
        end_page = re.search(r'a href="/security-centre.html\?start=(\d+?)" class="pagenav hasTooltip" title="End"',
                             data).group(1)
    except:
        exit('[-] Could not parse the end of page: ')

    end_page = int(end_page)
    for i in range(1, int(end_page / 10 + 1)):
        list_link.append(f"https://developer.joomla.org/security-centre.html?start={i * 10}")
        return list_link


# =================== Main =================== #
if __name__ == '__main__':
    # ++++++++ Get source spot ++++++++ #
    # source = get_html(URL)
    if isfile('resouce.html'):
        text = get_html(URL)
        f = open('resource.html', 'w', encoding='UTF8')
        f.write(text)
        f.close()
    source = open('resource.html', 'r', encoding='utf8').read()
    # print(source)
    # -------- End source spot -------- #

    # ++++++++ Start Parsing ++++++++ #
    test = parse_part(source)
    for i in test:
        parse_to_database(i)
        # print(i)
    # print(test)
    # === Done === #
    # list_pages = get_page_links(text) # Done
    # -------- End Parsing -------- #
