import math

x = 2**1000

stringy = str(x)
#print(len(stringy))
total = 0
for i in range (0,len(stringy)):
    temp = int(stringy[i])
    total = total + temp


print (total)
    

