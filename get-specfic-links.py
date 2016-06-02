#!/usr/bin/env python3
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys
import json


url = str(sys.argv[1])
print url

mydict = {}

def scrap(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    div = soup.find('div', id='srchRslt')
    for link in div.findAll('a'):
         name = (link.string)
         href = (link.get('href'))
         href = 'https://www.1mg.com' + str(href)
         mydict[str(name)] = str(href)        

scrap(url)


data = json.dumps([{'name': key, 'url': value} for key,value in mydict.items()], indent=4)
print(data)

