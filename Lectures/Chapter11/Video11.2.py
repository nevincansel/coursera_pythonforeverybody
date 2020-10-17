import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)     # [0-9]+ -> satırdaki sayılara bakıyor.   
print(y)    # Sonuçta çıkan sayılar liste içinde string olarak çıkıyor.
y = re.findall('[AEIOU]+', x)   # [AEIOU]+ -> satırdaki büyük sesli harflere bakıyor.
print(y)
y = re.findall('[aeiou]+', x)   # [aeiou]+ -> satırdaki büyük sesli harflere bakıyor.
print(y)


import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)  # Greedy. Sonuncu iki noktaya kadar gidiyor. Prefers longest
print(y)

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)     # Non-Greedy. Soru işareti greedy olma diyor ve From'dan sonra gelen iki noktada duruyor. Prefers shortest.
print(y)


import re
x = 'From cansel.efendioglu@enerjisa.com Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@+\S+', x)
print(y)
y = re.findall('^From (\S+?@+\S+)', x)    # findall'un içindeki parantez çıkacak sonucun nerde başlayıp nerde biteceğini gösteriyor. Bu yüzden From print edilmiyor.
print(y)



data = 'From cansel.efendioglu@enerjisa.com Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)   # atpos'tan sonraki ilk boşluğu bul
print(sppos)
host = data[atpos+1 : sppos]
print(host)


data = 'From cansel.efendioglu@enerjisa.com Sat Jan 5 09:14:16 2008'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


import re
line = 'From cansel.efendioglu@enerjisa.com Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)    # [^ ] -> Non-blank character, * -> many of them
print(y)
y = re.findall('^From .*@([^ ]*)', line)
print(y)



import re
file = open('mbox-short.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))


import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)  # \ karakteri doların regex yerine dolar olarak alınmasını sağladı.
print(y)