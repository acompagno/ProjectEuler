def pent_num(n):
	return (n*((3*n)-1))/2

def pent_check(x):
	a = .5+(.25+(4*1.5*x))**(.5)
	if a % 3 == 0:
		return True
	else:
		return False

n = 1
while True:
	temp = pent_num(n)
	for a in range (0,n):
		b = pent_num(n) - pent_num(a)
		if pent_check(b):
			c = pent_num(n) + b
			if pent_check(c):
				print (n,b,pent_num(n)-b)
	n = n + 1
