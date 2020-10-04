tot = 0
count = 0
while True :
    sval = input('Enter a number: ')
    if sval == 'Done' :
        break
    try : 
        fval = float(sval)
    except :
        print ('Please enter a number!')
    tot = tot + fval
    count = count + 1    
average = tot / count
print(count, tot, average)

