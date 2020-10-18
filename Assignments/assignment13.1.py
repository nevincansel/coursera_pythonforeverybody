import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:', len(lst))
total = 0
for item in lst:
    note = item.find('count').text
    note = int(note)
    total = total + note
print('Sum:', total)