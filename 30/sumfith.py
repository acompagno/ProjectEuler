i = 10
sumall = 0
while True :
    sumofdig = 0
    stringy = str(i)
    for a in range (0,len(stringy)):
        temp = int(stringy[a])
        sumofdig = sumofdig + temp**5
    if sumofdig == i:
        sumall = sumall + i
        print('i=',i)
        print(sumall)
    i = i +1
        
        
    
