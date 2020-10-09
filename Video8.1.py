for i in [5, 4, 3, 2, 1]: # list
    print(i)


friends = ['Cansu', 'Sinem', 'Eda']
for friend in friends:
    print('I love you', friend)

print(friends[1])
print(len(friends)) # list'in içinde kaç element olduğunu veriyor.
print(range(len(friends)))

# The range function returns a list that range from zero to one less than the parameter.
#range(4) = [0, 1, 2, 3]

for i in range(len(friends)): #counted loops
    friend = friends[i]
    print('I love you', friend)

