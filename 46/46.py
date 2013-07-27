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

def fit_char(n):
	for i in range(2,n):
		temp = n - i
		if (((temp/2)**.5)%1 == 0 and isprime(i)):
			return True
	return False


def main():
	i = 3
	while True:
		if not fit_char(i) and not isprime(i):
			return i
		i = i + 2

print("Answer:",main())
test2 = float(time.time())
print(test2 - test)