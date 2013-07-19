


f = open('names.txt','r')
x = f.read()

words = x.split()
words.sort()

total = 0 
for i in range (0,len(words)):
	temp_string =str(words[i])
	#print(temp_string)
	total_temp = 0
	for x in range (0,len(temp_string)):
		letter_value = ord(temp_string[x])-64
		total_temp = total_temp + letter_value
	total_temp =  total_temp * (i+1)
	total = total + total_temp

	

print (total)
