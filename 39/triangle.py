def check(a,b,c):
    if(a**2+b**2==c**2):
        return True
    else:
        return False

best = 0
p_best = 0
for p in range (1,1001):
    count = 0
    for a in range (1,p):
        for b in range (1,p-a):
            c = p-a-b
            if check(a,b,c):
                count = count+1
                #print ("p=",p,"a=",a,"b=",b,"c=",c,"count=",count)
    if count > best:
        best = count
        p_best=p
        print (p_best,best)

print (p_best,best)
            
            

        
        
