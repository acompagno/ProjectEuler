total=1
for i in range (1,100):
    total = total * i
print(total)

stringy =str(total)

sums= 0
for i in range (0,len(stringy)):
    temp = int(stringy[i])
    sums = sums + temp


print (sums)
    


    
