# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
pos = 18
tags = soup('a')
url = tags[pos-1].get('href', None)
print url

# Retrieve all of the anchor tags
n = 6
tags = soup('a')
for i in range(0,n):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos-1].get('href', None)
    print url

name = re.findall("by_(.*).html",url)
print name[0]
