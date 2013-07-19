i = 1
decimal = ''
while len(decimal) < 1000002:
	temp = str(i)
	decimal = decimal + temp
	i = i + 1

d_1 = int(decimal[0])
d_10 = int(decimal[9])
d_100 = int(decimal[99])
d_1000 = int(decimal[999])
d_10000 = int(decimal[9999])
d_100000 = int(decimal[99999])
d_1000000 = int(decimal[999999])

print(d_1,d_10,d_100,d_1000,d_10000,d_100000,d_1000000)
print(d_1*d_10*d_100*d_1000*d_10000*d_100000*d_1000000)
