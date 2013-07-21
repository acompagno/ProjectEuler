def ispalindrome(n):
    return n == int(str(n)[::-1])

def isLychrel(n):
	count =0
	while count <= 50:
		n = n+int(str(n)[::-1])
		if (ispalindrome(n)):
			return False
		count = count + 1
	return True

total = 0
for i in range (0,10000):
	if isLychrel(i):
		total = total +1
		print(i)

print(total)
