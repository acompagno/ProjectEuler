def pancheck(a):
	length = len(a)
	if length != 9:
		return False
	a9 = [1,2,3,4,5,6,7,8,9]
	q=[]
	for i in range(0,len(a)):
		temp = int(a[i])
		q.append(temp)
	q.sort()
	if length == 9:
		if q == a9:
			return True
	else:
		return False


best = 0
for i in range (1,999999):
	b=''
	for x in range (1,3):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,4):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,5):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,6):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,7):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,8):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,9):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp

for i in range (1,999999):
	b=''
	for x in range (1,10):
		a = str(i*x)
		b=b+a
	if pancheck(b):
		temp=int(b)
		if temp > best:
			best = temp
print(best)