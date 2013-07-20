def factorial(x):
        if x == 0:
                return 1
        fac=1
        for i in range (1,x+1):
                fac=fac*i
        return fac

def comb(n,r):
	top = factorial(n)
	bottom_1 = factorial(r)
	minus = n-r
	bottom_2 = factorial(minus)
	c = top / (bottom_1*bottom_2)
	return c

count = 0
for n in range (1,101):
	for r in range (1,n):
		com = comb(n,r)
		if com > 1000000:
			count=count+1


print(count)
