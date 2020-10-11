name = input('Enter file: ')
try:
    file = open(name)
except:
    print('File', file, 'cannot be opened.')
    quit()

mails = dict()
for line in file:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    mails[email] = mails.get(email,0) + 1

largest = -1
theword = None
for k,v in mails.items():
    if v > largest:
        largest = v
        theword = k
print(theword, largest)

#mostmail = max(mails, key=mails.get)
#print(mostmail, mails[mostmail])
    
