import re
file = open('regex.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    i = 0
    for number in num:
        number = num[i]
        number = int(number)
        i = i + 1
        numlist.append(number)
print(sum(numlist))
