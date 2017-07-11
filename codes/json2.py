import urllib
import json

url = raw_input('Enter url:')
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

comments = js["comments"]

sum = 0
for comment in comments:
    sum = sum + int(comment['count'])
print sum
