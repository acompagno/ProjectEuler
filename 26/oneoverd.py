best=0
bestd=0

for d in range (1,1001):
    temp = 1/10
    count=0
    q=[]
    #print(d)
    for i in range(0,d):
        temp=(int(temp*10))%d
        if temp not in q :
            q.append(temp)
            count = count + 1
    #print(q,d)
    if count>best:
        best = count
        bestd=d


print (best,bestd)

    
