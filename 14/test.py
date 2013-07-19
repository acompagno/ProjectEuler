def sequence(i):
    counter=0
    temp=i
    print(i)
    while i != 1:
        if i%2 == 0:
            i=i/2
            counter = counter+1
            print(i)
        else:
            i=3*i+1
            counter = counter+1
            print(i)
    return counter+1

print(sequence(983))


