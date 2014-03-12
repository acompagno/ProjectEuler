def main():
	sums , square = 0 , 0
	for i in range(101):
		sums = sums + i
		square = square + i**2
	print(sums**2 - square)

main()
