fname = input('Enter a file name: ')
try:
    file = open(fname)
except:
    print('File', fname, 'cannot be opened.')
    quit()

total = 0
count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    posz = line.find('0')
    num = line[posz:]
    total = total + float(num)
    average = total / count
print('Average spam confidence:', average)

