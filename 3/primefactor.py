import math
def prime(x):
    z=0
    for b in range(2,x):
        #print(b)
        if(x%b == 0):
            #print("FACTOR",b)
            z+=1
    if(z==0):
        return 0
    else:
        return 1

x = 10
for i in range(1,600851475143//2):
    if(600851475143%i == 0):
        x = prime(i)
    if(x == 0):
        print(i)
    x  = 10
            
