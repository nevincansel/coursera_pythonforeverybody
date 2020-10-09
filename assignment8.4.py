fname = input('Enter file name: ')
try:
    file = open(fname)
except:
    print('File', fname, 'cannot be opened.')
    quit()

lst = list()
for line in file:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        word = words[i]
        if word in lst:
            continue
        lst.append(word)
        lst.sort()
print(lst)