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

def test(a,b):
	y=2
	x=0
	best_a = 0
	best_b = 0
	best_count = 0
	while isprime(y):
		y = (x**2) + (a*x) + (b)
		x = x + 1
	return x - 2

best=0
best_a = 0
best_b = 0
for a in range (-999,1000):
	for b in range (-999,1000):
		temp = test(a,b)
		if temp > best:
			best = temp
			best_a = a
			best_b = b


print(best,best_a,best_b,best_a*best_b)


