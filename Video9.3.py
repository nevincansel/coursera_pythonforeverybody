counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print ('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])


counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key, value in counts.items():
    print(key, value)

print(counts.keys())
print(counts.values())
print(counts.items())





