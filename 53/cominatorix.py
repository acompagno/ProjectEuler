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

print(comb(23,10))
