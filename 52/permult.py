def check(a,b): 
	# a - original b - multiple
	list_a = []
	list_b = []
	str_a = str(a)
	str_b = str(b)
	if len(str_a) != len(str_b):
		return False
	for i in range (0,len(str_a)):
		list_a.append(str_a[i])
		list_b.append(str_b[i])
	list_a.sort()
	list_b.sort()	
	if list_a == list_b:
		return True
	else:
		return False

a = 1
while True:
	if check(a,2*a) and check(a,3*a) and check(a,4*a) and check(a,5*a) and check(a,6*a):
		print(a)
		break 
	a = a +1
