def check(a,b,c):
    if(a**2+b**2==c**2):
        return True
    else:
        return False

def lol(p):
    best = 0
    p_best = 0
    count = 0
    for a in range (1,p):
        for b in range (1,p-a):
            c = p-a-b
            #print(a,b,c,a+b+c)
            if check(a,b,c):
                print(a,b,c)


lol(240)
