def main ():
	largest = 0 
	for i in range(999 , 99 , -1):
		for b in range(i , 99 , -1):
			tmp = i * b
			if (str(tmp)[::-1] == str(tmp) and tmp > largest):
				largest = tmp
				break
	print(largest)


main()
