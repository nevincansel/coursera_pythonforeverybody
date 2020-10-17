import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)
print('Retrieving', url)
click = 1
while click <= count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    urls = list()
    for tag in tags:
        tag = tag.get('href', None)
        urls.append(tag)
    url = urls[position-1]
    print('Retrieving', url)
    urllib.request.urlopen(url) 
    click = click + 1