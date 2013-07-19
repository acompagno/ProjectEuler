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

total = 0
a = 0
while a < 2000000:
    if isprime(a):
        total = total+a
    a=a+1

print (total)
        
