def check_pow (n,power):
	if len(str(n)) == power:
		return True 


count = 0
for n in range (1,10000):
	for power in range (1,10000):
		if check_pow(n**power,power):
			count += 1
			print ("count",count,"n",n,"power",power,"number",n**power)





