def ispalindrome(n):
    return n == n[::-1]


total = 0
for i in range (1,1000000):
		str_i = str(i)
		str_temp = bin(i)
		str_int = str_temp[2::]
		if ispalindrome(str_i) and ispalindrome(str_int):
			total = total + i

print(total)
