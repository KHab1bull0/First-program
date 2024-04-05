from random import randint

p = 1

n = randint(2, 4294967295)
change = True

print(n)

while 1:
    if change == True:
        sar = int(input("sardor: "))
        p = p * sar
        change = False
        if p > n:
            print('sardor yutdi')
            break
    elif change == False:
        odina = int(input("odina: "))
        p = p * odina
        change = True
        if p > n:
            print('odina yutdi')
            break
    
    

