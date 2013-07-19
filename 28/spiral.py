total = 1
temp = 1
for i in range (1,501):
    for x in range(0,4):
        temp = temp + i*2
        total = total + temp

print(total)
