import time 
test = float(time.time())

def primefac(n):
	primes=[]
	a=n
	while not isprime(a):
		for i in range (2,n//2+1):
			if isprime(i) and a%i == 0:
				primes.append(i)
				a=a//i
				break
	primes.append(a)
	return primes

def isprime(x):
	if x in primelist:
		return True
	if x < 2:
		return "Less 2", False
	elif x == 2:
		primelist.append(x)
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return False
		primelist.append(x)
		return True

def getdivsum(n):
	primes = primefac(n)
	total = 1
	used = [];
	for i in range (0,len(primes)):
		if (primes[i] in used ):
			continue
		else:
			temp_sum = 0
			temp_pow = primes.count(primes[i])
			for j in range (0,temp_pow+1):
				temp_sum = temp_sum + primes[i]**j
			used.append(primes[i])
			total = temp_sum * total
	return total - n

def isab(n):
	if n < 12 :
		return False 
	if n in ablist:
		return True
	elif getdivsum(n)>n:
		ablist.append(n)
		return True
	else:
		return False

def fit_criteria(n):
	if n < 24:
		return True 
	if n in false_list:
		false_list.remove(n)
		return False
	z = 0
	while (z < len(ablist) and ablist[z] < n):
		if (ablist[z] < n):
			if isab(n - ablist[z]):
				return False
		z = z +1
	return True

def main():
	false_list = []
	total = 0
	temp2 = 0
	f = 0
	#Loading List of abundant numbers
	for i in range (12,28124):
		isab(i)
	print("Ablist" , len(ablist))
	test2 = float(time.time())
	print(test2 - test)

	#Adding Values to False List
	for v in range (0,len(ablist)):
		if ablist[v]*2 > 28123:
			break
		false_list.append(ablist[v]*2)
	print("False List x2" , len(false_list))
	test2 = float(time.time())
	print(test2 - test)
	
	#Adding Values to False List
	for e in range (0,len(ablist)):
		for f in range(e+1,len(ablist)):
			if (ablist[e]+ablist[f] >28123):
				break
			else :
				false_list.append(ablist[e]+ablist[f] )
	false_list = sorted(set(false_list))
	print("False list addition" , len(false_list))
	test2 = float(time.time())
	print(test2 - test)
	
	# Sorting false_list
	false_list.sort
	print("list sorted")
	test2 = float(time.time())
	print(test2 - test)

	#Finding answer
	count = 0
	for x in range (0,28123):
		if x not in false_list:
			total = total + x 
			count = count + 1	
	return total


primelist = []
ablist = []
all_list = []
false_list = []
print("Answer",main())
test2 = float(time.time())
print(test2 - test)
