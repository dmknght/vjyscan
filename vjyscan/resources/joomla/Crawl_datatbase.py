# Source: https://developer.joomla.org/security-centre.html?start=120
from os.path import isfile
import requests
import re
# Static Variable
URL = 'https://developer.joomla.org/security-centre.html'

# =================== Parse Part =================== #
def parse_to_database(data):
    name = re.search(r'Core[ -]{3}(.+?) </h2>', data).group(1)
    if "CVE Number:" not in source:
        CVE = "Empty"
    else:
        CVE = re.search(r'<li><strong>CVE Number:</strong>[ ]{0,}(.+?)[ ]{0,}</li>', data).group(1)
    # Need to do the reqirement for version, read the __init__
    version = re.search(r'<li><strong>Versions:[ ]{1,}</strong>(.+?)</li>', data).group(1)
    version = re.sub('[ -]{2,}| through ', "<=", version)
    return {"name": name, "CVE": CVE, "version": version}

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
        return "Empty"
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
        end_page = re.search(r'a href="/security-centre.html\?start=(\d+?)" class="pagenav hasTooltip" title="End"', data).group(1)
    except:
        exit('[-] Could not parse the end of page. Need to improve the code')
    finally:
        end_page = int(end_page)
        for i in range(1, int(end_page/10+1)):
            list_link.append(f"https://developer.joomla.org/security-centre.html?start={i*10}")
            return list_link

# =================== Main =================== #
if __name__=='__main__':
    list_database = []
    source = get_html(URL)
    # Testing
    test = parse_part(source)
    for i in test:
        list_database.append(i)
    if isfile('core.jdb') == False:
        open('core.jdb', 'w').close()
    with open('core.jdb', 'a') as file:
        database = file.read()
        for i in test:
            if i in database:
                pass
            else:
                file.write(i)

# To do in here, re-make the test part to another function
# Do requirement for version
# parse other links, code got all the other pages link in get_page_links()

