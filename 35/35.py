import time 
import collections
test = float(time.time())
# num = 123456
# print(list(str(num)))
# print("".join(list(str(num))))
# print(int("".join(list(str(num)))))
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

def iscircprime(n):
	d = collections.deque(str(n))
	for i in range (0,len(str(n))):
		if not isprime(int("".join(list(d)))):
			return False
		d.rotate(1)
	return True

def main():
	count = 0
	for i in range (2,1000000):
		if iscircprime(i):
			count = count +1
	return count

print(main())
test2 = float(time.time())
print(test2 - test)