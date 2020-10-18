import urllib.request
import urllib.parse
import urllib.error
import json


url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
comments = info['comments']
print('Count:', len(comments))
total = 0
for item in comments:
    note = item['count']
    note = int(note)
    total = total + note
print('Sum', total)