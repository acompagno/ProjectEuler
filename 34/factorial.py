def factorial(x):
    fac=1
    for i in range (1,x+1):
        fac=fac*i
    return fac
def test(b):
    stringy = str(b)
    length =  len(stringy)
    total=0
    for c in range (0,length):
        r = int(stringy[c])
        temp = factorial(r)
        total = total + temp
    if total == b:
        return True
    else:
        return False
        

x=10
sums = 0
while True:
    #print(x)
    if test(x):
        sums = sums + x
        print (sums , x)
    x=x+1
    
    
    
#print(factorial(4))
