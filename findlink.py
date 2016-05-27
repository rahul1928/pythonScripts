#!/usr/bin/env python3
from BeautifulSoup import BeautifulSoup
import urllib2
import re

import sys

url = str(sys.argv[1])
print url
html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print (link.get('href'))
