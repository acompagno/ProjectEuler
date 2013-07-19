def divs(a):
	q=[1]
	for i in range (2,a//2+1):
		if a%i==0:
			q.append(i)
	return q


alist=[]
blist=[]
for a in range (1,10000):
	b = sum(divs(a))
	if sum(divs(b)) == a and b !=a and b not in alist :
			print(a,b)
			alist.append(a)
			blist.append(b)

print(sum(alist)+sum(blist))