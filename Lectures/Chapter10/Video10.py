x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

(x , y) = ('Burkay', 'Cansel')
print(y, 'is the best!!')


d = {'a' : 10, 'b' : 1, 'c' : 22}
d.items()
s = sorted(d.items()) # key'e göre sıralıyor.
print(s)

c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp=sorted(tmp, reverse=True) # büyükten küçüğe sıralaması için reverse=True ekledik.
print(tmp)


file=open('romeo.txt')
counts=dict()
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst=list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)


c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v, k) for k,v in c.items()], reverse=True))


