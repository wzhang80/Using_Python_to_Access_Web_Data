import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ')
#print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
#print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')
s = 0
for item in lst:
    s = s + int(item.text)
print s
#lat = results[0].find('geometry').find('location').find('lat').text
#lng = results[0].find('geometry').find('location').find('lng').text
#location = results[0].find('formatted_address').text
#print 'lat',lat,'lng',lng
#print location
