def test (a):
    temp = 0
    b=0
    for i in range (9, - 1,-1):
        temp2 = a[b]*(10**i)
        temp = temp + temp2
        b = b+1
    print(temp)

a =[0,1,2,3,4,5,6,7,8,9]
test(a)

