def tri_num(n):
	return (n*(n+1))/2

def pent_num(n):
	return (n*((3*n)-1))/2

def hex_num(n):
	return n*((2*n)-1)

def tri_check(x):
	a = (-.5)+((.25+(4*.5*x))**(.5))
	if a % 1 == 0:
		return True
	else:
		return False

def pent_check(x):
	a = .5+(.25+(4*1.5*x))**(.5)
	if a % 3 == 0:
		return True
	else:
		return False


n = 143

while True:
	temp = hex_num(n)
	if tri_check(temp) and pent_check(temp):
		print(temp)
	n = n + 1