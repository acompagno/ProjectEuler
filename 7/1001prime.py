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

i=2
x=0
while x<10001:
    #print(i,"x=",x)
    if isprime(i) :
        #print(i,x)
        x= x+1
        prime_temp = i
    i= i+1


print(prime_temp , x)
    
    
