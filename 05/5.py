def main():
	i = 20
	while (not isDivByRange20(i)):
		i = i + 20
	print(i)

def isDivByRange20(n):
	for i in range(20 , 2 , -1):
		if (n % i != 0):
			return False
	return True;

main()
