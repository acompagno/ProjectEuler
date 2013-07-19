def isprime(x):
	x = abs(int(x))
	if x < 2:
		return False
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return False
		return True

def truncforward(n):
	count = 0
	str_temp=str(n)
	for i in range(0,len(str_temp)):
		temp = int(str_temp[i:len(str_temp)+1])
		#print(temp)
		if isprime(temp):
			count = count + 1
	if count == len(str_temp):
		return True 
	else:
		return False	

def truncbackwards(n):
	count = 0
	str_temp=str(n)
	for i in range(1,len(str_temp)+1):
		temp = int(str_temp[0:i])
		#print(temp)
		if isprime(temp):
			count = count + 1
	if count == len(str_temp):
		return True 
	else:
		return False	


total = 0
i = 11
count = 0
while True:
	if isprime(i) and truncforward(i) and truncbackwards(i):
		total = total + i
		count = count + 1
		print (count,i,total)
	i = i + 2
		
