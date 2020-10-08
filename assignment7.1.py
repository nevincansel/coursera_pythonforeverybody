fname = input('Enter file name: ')
try:
    file = open(fname)
except:
    print('File', fname, 'cannot be opened.')
    quit()

for line in file:
    line = line.rstrip()
    print(line.upper())