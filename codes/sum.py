import re

filename = 'regex_sum_373007.txt'
hand = open(filename)
s = 0
for line in hand:
    stuff = re.findall('[0-9]+',line)
    if len(stuff)>0 :
        for nstr in stuff:
            num = int(nstr)
            s = s + num
print s

