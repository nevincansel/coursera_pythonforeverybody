fruit = 'banana'
length = len(fruit) #kelimenin uzunluğunu gösteriyor.
result = 'm' in fruit
pos = fruit.find('na') #na harflerinin ilk pozisyonunu gösteriyor.
print(pos)
print(result)
print(length)


greet = 'Hello Bob'
zap = greet.lower() #metnin tüm karakterlerini küçültüyor.
print(zap)
bap = greet.upper() #metnin tüm karakterlerini büyütüyor.
print(bap)
nstr = greet.replace('Bob','Jane') #verilen değerleri değiştiriyor.
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

print('Hi There'.lower())

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff)) #stuff ile yapabileceklerimizin listesini veriyor.


greet = ' Hello Bob'
nstr = greet.lstrip() #stringin başındaki boşlukları siliyor.
print(nstr)
greet = 'Hello Bob '
nstr = greet.rstrip() #stringin sonundaki boşlukları siliyor.
print(nstr)
greet = ' Hello Bob '
nstr = greet.strip() #stringin sonundaki ve başındaki boşlukları siliyor.
print(nstr)

line = 'Please have a nice day'
print(line.startswith('Please')) #kelimenin parantez içinde verilenle başlayıp başlamadığını kontrol ediyor.
print(line.startswith('p'))

data = 'From cansel.efendioglu@enerjisa.com Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos) #atposun pozisyonundan sonraki ilk boşluğun pozisyonunu verir.
print(sppos)
host = data[atpos+1:sppos] #atpos'tan bir sonraki karakterden başlayarak sonraki boşluğa kadar olan tüm karakterleri verir.
print(host)


