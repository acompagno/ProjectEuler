import time 
test = float(time.time())
def isprime(x):
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

def main():
	best_count,best_val = 0,0
	primes = []
	for i in range (2,1000000):
		if isprime(i):
			primes.append(i)
	print("Primes List Done")
	# print(primes)
	test2 = float(time.time())
	print(test2 - test)

	for i in range(0,len(primes)):
		temp = 0
		if len(primes) - i < best_count:
			break
		for j in range(i,len(primes)):
			temp = temp + primes[j]
			if temp>=1000000:
				break
			if temp in primes and (j-i) > best_count:
				best_count = j
				best_val = temp
				print(best_val,best_count,j,i)
	print(best_count,best_val)

main()
test2 = float(time.time())
print(test2 - test)