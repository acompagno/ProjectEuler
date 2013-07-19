answer_a = 1
answer_b = 1
for a in range (10,100):
    for b in range (10,100):
        string_a = str(a)
        string_b = str(b)
        for i in range (0,2):
            for x in range (0,2):
                if a%10 == 0 or b%10 ==0:
                    continue
                a_el=int(string_a[i])
                b_el=int(string_b[x])
                a_new = a-((a_el)*(10**(1-i)))
                b_new = b-((b_el)*(10**(1-x)))
                if a_new%10 == 0:
                    a_new = a_new//10  
                if b_new%10 == 0:
                    b_new = b_new//10  
                #print('a',a,'b',b,'a_el',a_el,"b_el",b_el,"b_new",b_new,"a_new",a_new)
                if b_new == 0:
                    continue 
                if a_el == b_el and a_new/b_new == a/b and a != b and a<b :
                    print(a,b,a_new,b_new)
                    answer_a = answer_a*a_new
                    answer_b = answer_b*b_new
print (answer_a,answer_b)
