a = [1, 2, 3]
b = [4, 5 ,6]
c = a + b
print(c)


stuff = list() # stuff adında boş bir liste oluşturdum.
stuff.append('book') # listeye book adında bir element ekledim.
stuff.append(99) # yeni elementler listenin sonuna eklenir.
print(stuff)

# in ve not in, elementin listede olup olmadığını araştırmak için kullanılır.

friends = ['Cansu', 'Sinem', 'Eda']
friends.sort() # elementleri alfabetik olarak sıralıyor.
print(friends)


nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


# daha az memory kullanıyor.
total = 0 
count= 0
while True:
    inp = input('Enter a number: ') 
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)


# daha çok memory kullanıyor.
numlist=list()
while True:
    inp = input('Enter a number: ') 
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)


