file = open('example.txt') #open() dosyayı açmak için kullanılıyor.
for cheese in file :
    cheese = cheese.rstrip() #rstrip ile satırın sonundaki new line'dan kurtuluyoruz.
    print(cheese) 
    
    
# print her satırı bir alta yazıyor ancak her satırın sonunda zaten new line var. 
# Bu nedenle dosyayı print ederken arada ekstra boşluk oluşuyor.



file = open('example.txt') 
count = 0
for line in file:   #for döngüsü her satır satır sayıyor ve toplamda kaç satır olduğunu gösteriyor.
    count = count + 1
print('Line count:', count)


file = open('example.txt')
inp = file.read() #read() tüm dosyayı tek bir string gibi okuyor.
print(len(inp)) #tüm dosyanın toplam karakter sayısını veriyor.
print(inp[:20])

file = open('example.txt')
for line in file:
    line = line.rstrip()
    if line.startswith('Benim'):
        print(line)

file = open('example.txt')
for line in file:
    line = line.rstrip()
    if not line.startswith('Benim'):
        continue
    print(line)


file = open('example.txt')
for line in file:
    line = line.rstrip()
    if not 'Rize' in line :
        continue
    print(line)


fname = input('Please enter a file name: ')
try: 
    file = open(fname)
except:
    print('File', fname, 'cannot be opened')
    quit()

count = 0
for line in file:
    if line.startswith('Ben') :
        count = count + 1
print('There is' , count, 'Ben in', fname)





