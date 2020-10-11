name = input('Enter file: ')
try:
    file = open(name)
except:
    print('File', file, 'cannot be opened.')
    quit()

hours = dict()
for line in file:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[5].split(':')
    hour = words[0]
    hours[hour] = hours.get(hour, 0) + 1

for key, val in sorted(hours.items()):
    print(key,val)