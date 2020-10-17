import urllib.request
import urllib.parse
import urllib.error
import re

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
text = list()
for line in fhand:
    lines = line.decode().strip()
    text.append(lines)
link_line = text[3]
qpos1 = link_line.find('"')
qpos2 = link_line.find('>', qpos1)
link = link_line[qpos1+1 : qpos2-1]
page = urllib.request.urlopen(link)
for line in page:
    print(line.decode().strip())


fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in fhand:
    line = line.decode().strip()
    if line.startswith('<a'):
        link = re.findall('href="(.+)"', line)
print(link)


    

