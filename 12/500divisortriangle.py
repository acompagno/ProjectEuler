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
	return primes

def divisors(n):
	primes =  primefac(n)
	u_primes = list(set(primes))
	temp = 0
	div = 1
	for i in range(0,len(u_primes)):
		temp =  primes.count(u_primes[i])
		div = div * (temp+1)
	return div

total = 0
temp = 0
div = 0
while div <500 :
    temp = temp +1
    total = total + temp
    if total % 2 != 0 :
        continue 
    div = divisors(total)

print (total)


