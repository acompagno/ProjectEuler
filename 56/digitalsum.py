def digi_sum(c):
	str_c = str(c)
	total = 0
	for i in range(0,len(str_c)):
		total = total + int(str_c[i]) 
	return total

best = 0
for a in range(1,100):
	for b in range(1,100):
		temp = digi_sum(a**b)
		if temp > best:
			best = temp

print(best)


