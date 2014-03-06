a,b,total= 0,1,0
for i in range (0,4000000):
	current = a + b
	b = a
	a = current 
	if current >= 4000000:
		break
	if current < 4000000 and  current % 2 == 0:
		total = total + current
print("Answer:",total)