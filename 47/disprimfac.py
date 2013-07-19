def isprime(x):
	x = abs(int(x))
	if x < 2:
		return "Less 2", False
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return False
		return True


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
	primes = list(set(primes))
	return primes

n = 210
while True:
	#print(n)
	temp = primefac(n)
	if len(temp) != 4:
		n = n+1
		continue
	else:
		temp = primefac(n+1)
		if len(temp) != 4:
			n = n+1
			continue
		else :
			temp = primefac(n+2)
			if len(temp) != 4:
				n = n+1
				continue
			else:
				temp = primefac(n+3)
				if len(temp) != 4:
					n = n+1
					continue
				else:
					print(n)
					break
