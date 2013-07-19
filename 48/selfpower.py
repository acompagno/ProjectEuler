total = 0
for i in range (1,1001):
	total = total + (i)**(i)

total_list = str(total)
print(total_list[len(total_list)-10:len(total_list)])