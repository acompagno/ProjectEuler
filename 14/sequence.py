def sequence(i):
    counter=0
    temp=i
    while i != 1:
        if i%2 == 0:
            i=i/2
            counter = counter+1
        else:
            i=3*i+1
            counter = counter+1
    return counter+1


counter_best = 0
i_best = 0
for i in range (2,1000000):
    temp = sequence(i)
    #if i == 500000:
     #   print(i)
    if temp > counter_best:
        counter_best = temp
        i_best = i
      #  print(i)

print(counter_best,i_best)
    
