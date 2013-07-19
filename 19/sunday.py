months = [31,28,31,30,31,30,31,31,30,31,30,31]
months_leap = [31,29,31,30,31,30,31,31,30,31,30,31] #if year%4 == 0 or year%400 == 0
#days 1 : Monday - 7:Sunday 
count = 0
rem_total = 1
rem = 1
for y in range (1901,2001):
	for m in range (0,12):
		if y%4 == 0 and y%100 != 0:
			rem = 7 - (months_leap[m]-rem)%7
		elif y%400 == 0:
			rem = 7 - (months_leap[m]-rem)%7
		else:
			rem = 7 - (months[m]-rem)%7			
		if rem == 0 or rem ==7:
			count = count + 1

print(count-2)