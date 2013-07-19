import math
numbers = []
c = 0
for a in range(2,101):
    for b in range(2,101):
        d = math.pow(a,b)
        #print(d)
        numbers.append(d)
for i in range(len(list(set(numbers)))):
    c+=1

#print(numbers)
print(c)
