import math

def isPrime(n):
	if (n < 4):
		return True;
	for i in range(3 , int(n**(0.5)) + 1 , 2):
		if (n%i == 0):
			return False
	return True

def main():
	num = 600851475143
	for i in range(3 , int(num**(0.5)) + 1 , 2):
		if (num % i == 0 and isPrime(i)):
			print(i)

main()        
