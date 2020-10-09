fname = input('Enter a file name: ')
try:
    file = open(fname)
except:
    print('File', fname, 'cannot be opened.')
    quit()

count = 0
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    count = count + 1
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')