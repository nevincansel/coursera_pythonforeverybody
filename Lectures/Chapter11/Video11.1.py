import re
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# Üssteki ve alttaki aynı sonucu veriyor.

file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

####################################


file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Üssteki ve alttaki aynı sonucu veriyor.

import re
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):   # ^From -> From ile başlayan satırlara bak.
        print(line)

####################################

import re
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('^X.*:', line):    # X ile başlayan ve herhangi bir karakterle devam edip iki nokta ile biten satırlara bak.
        print(line)


import re
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('^X-\S+:', line):  # ^X- kısmı X- ile başlayanları ifade ediyor. \S boşluk olmasın demek. Sondaki + ise >=1 anlamına geliyor. 
        print(line)                 #   Yani X- ile başlayan ve bir ya da birden fazla boşluk içermeyen satırları al.
        