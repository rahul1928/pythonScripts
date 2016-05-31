#!/usr/bin/env python3
from BeautifulSoup import BeautifulSoup
import urllib2
import re

import sys

url = str(sys.argv[1])
print url
html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)
div = soup.find('div', id='srchRslt')
for link in div.findAll('a'):
    name = (link.string)
    href = (link.get('href'))
    print str(name) + ' : ' + 'https://www.1mg.com' + str(href) 

