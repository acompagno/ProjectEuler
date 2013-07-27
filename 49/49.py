import itertools
import time 
test = float(time.time())

def isprime(x):
	if x < 2:
		return "Less 2", False
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return False
		return True

def fit_char(n):
	temp_list , new_list,last_list= list(itertools.permutations(str(n))),[],[]
	for i in range(0,len(temp_list)):
		new_list.append(int("".join(temp_list[i])))
	new_list.sort()
	for x in range(0,len(new_list)):
		if isprime(new_list[x]):
			last_list.append(new_list[x])
	for y in range (0,len(last_list)):
		for z in range (y , len(last_list)):
			for a in range(z , len(last_list)):
				if (last_list[y]-last_list[z] == last_list[z]-last_list[a] and last_list[y]-last_list[z]!=0 ):
					return True , int("".join(str(last_list[y])+str(last_list[z])+str(last_list[a])))
					# print(last_list[y],last_list[z],last_list[a])
	return False , "False"
	print(last_list)

def main():
	for i in range(1000,10000):
		boo , ans = fit_char(i)
		temp_list = list(str(i))
		temp_list = [ int(x) for x in temp_list ]
		temp_list.sort()
		if boo and len(str(ans)) == 12 and temp_list != [1,4,7,8]:
			print(i)
			print("Answer:",ans)
			return

main()
test2 = float(time.time())
print(test2 - test)