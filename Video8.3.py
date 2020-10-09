abc = 'With three words'
stuff = abc.split() # stringi boşluklardan parçalara bölüp liste oluşturuyor.
print(stuff)
for w in stuff:
    print(w)


line = 'A lot       of spaces'
etc = line.split() 
print(etc)

line = 'first;second;third'
etc = line.split(';') # noktalı virgüle göre böl dediğim için oradan bölerek liste oluşturdu.
print(etc)

file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
host = pieces[1]
print(host)


