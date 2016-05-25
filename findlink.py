#!/usr/bin/env python3
from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("https://www.1mg.com/drugs-ailments")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print (link.get('href'))


