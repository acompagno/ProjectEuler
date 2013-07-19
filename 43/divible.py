import random
def test (a):
    temp = 0
    b=0
    for i in range (9, - 1,-1):
        temp2 = a[b]*(10**i)
        temp = temp + temp2
        b = b+1
    return temp
def prop (a):
    div = [2,3,5,7,11,13,17]
    x=0
    count = 0
    for i in range (1 , 8):
        num = (a[i]*(10**2) + a[i+1]*(10) + a[i+2])
        if num % div[x] == 0:
            count = count +1
        x = x+1
    if count == 7:
        return True
    else:
        return False
        
        
a =[0,1,2,3,4,5,6,7,8,9]
q = []
sums=0
while True:
    random.shuffle(a)
    #print(test(a))
    if a[0]==0:
        continue
    if prop(a):
        num = test(a)
        if num in q:
            continue
        else:
            q.append(num)
            sums = sums + num
            print ('num=',num,'sum=',sums)
    
        
    



