def pancheck(a,b,c):
	a_str = str(a)+str(b)+str(c)
	length = len(a_str)
	a9 = [1,2,3,4,5,6,7,8,9]
	q=[]
	for i in range(0,len(a_str)):
		temp = int(a_str[i])
		q.append(temp)
	q.sort()
	if length == 9:
		if q == a9:
			return True
	return False


z=[]
for a in range (1,9999):
	for b in range (1,9999):
		c = a*b
		if pancheck(a,b,c):
			if c not in z:
				z.append(c)
				print(a,b,c)

total =0 
for i in range (0,len(z)):
	total = total + z[i]

print(total)
