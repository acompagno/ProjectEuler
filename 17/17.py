import time 
test = float(time.time())

teens = ["eleven" , "twelve" , "thirteen" , "fourteen" , "fifteen" , "sixteen" , "seventeen" , "eighteen" , "nineteen"]
tens = ["ten" , "twenty" , "thirty" , "forty" , "fifty" , "sixty" , "seventy" , "eighty","ninety"]
first_ten = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"]

total = []
for i in range(1,1001):
	count = 0
	if i < 10:
		total.append(first_ten[i-1])
		count = count + 1
	if i> 10 and i<20:
		total.append(teens[i-11])
		count = count + 1
	if i <100 and i%10==0:
		count = count + 1
		total.append(tens[(i//10)-1])
	if i>20 and i < 100 and i % 10 != 0:
		count = count + 1
		total.append(tens[int(str(i)[0])-1]+" "+first_ten[int(str(i)[1])-1])
	if i%100 == 0 and i < 1000:
		count = count + 1
		total.append(first_ten[int(str(i)[0])-1]+" hundred")
	if i>100 and i < 1000 and i%100 < 10 and i%100 !=0:
		count = count + 1
		total.append(first_ten[int(str(i)[0])-1]+" hundred and "+first_ten[i%100-1])
	if i>100 and i < 1000 and i%10 == 0 and i%100 !=0:	
		count = count + 1
		total.append(first_ten[int(str(i)[0])-1]+" hundred and "+tens[(i%100)//10-1])
	if i>100 and i < 1000 and i%100 > 10 and i%100 < 20 :
		count = count + 1
		total.append(first_ten[int(str(i)[0])-1]+" hundred and "+teens[i%10-1])
	if i>100 and i < 1000 and i%100 > 20 and i%10!=0:
		count = count + 1
		total.append(first_ten[int(str(i)[0])-1]+" hundred and "+tens[(i%100)//10-1]+" "+first_ten[i%10-1])
	if i == 1000:
		count = count + 1
		total.append("one thousand")
	if count>1:
		print(i,count)

temp_list = list("".join(total))
answer = 0
for i in range (0,len(temp_list)):
	if temp_list[i] != ' ':
		answer = answer + 1
print("Answer" , answer)
test2 = float(time.time())
print("Completed in",test2 - test,"sec")