def isprime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def pancheck(a):
	a_str = str(a)
	length = len(a_str)
	a9 = [1,2,3,4,5,6,7,8,9]
	a8 = [1,2,3,4,5,6,7,8]
	a7 = [1,2,3,4,5,6,7]
	a6 = [1,2,3,4,5,6]
	a5 = [1,2,3,4,5]
	a4 = [1,2,3,4]
	a3 = [1,2,3]
	a2 = [1,2]
	a1 = [1]
	q=[]
	for i in range(0,len(a_str)):
		temp = int(a_str[i])
		q.append(temp)
	q.sort()
	if length == 9:
		if q == a9:
			return True
	if length == 8:
		if q == a8:
			return True
	if length == 7:	
		if q == a7:
			return True
	if length == 6:
		if q == a6:
			return True
	if length == 5:
		if q == a5:	
			return True
	if length == 4:
		if q == a4:
			return True
	if length == 3:
		if q == a3:
			return True
	if length == 2:
		if q == a2:
			return True
	else:
		return False


for i in range (7999999,0,-1):
	if pancheck(i):
		if isprime(i):
			print(i)
