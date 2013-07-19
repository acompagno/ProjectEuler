x=1
y=1
temp = 0
length = 0
place = 2


while length < 1000:
    temp = y + x
    x = y
    y = temp
    temps = str(y)
    length = len(temps)
    place = place + 1

print(place)    
    
