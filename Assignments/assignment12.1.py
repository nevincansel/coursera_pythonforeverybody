import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a url: ')    # http://py4e-data.dr-chuck.net/known_by_Davi.html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
count = 0
numlist = list()
for tag in tags:
    tag = tag.decode().strip()
    num = re.findall('[0-9]+', tag)
    number = int(num[0])
    numlist.append(number)
    count = count + 1

print('Sum', sum(numlist))
print('Count', count)