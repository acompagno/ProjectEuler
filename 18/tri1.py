a=[75]
b=[95,64]
c=[17, 47 ,82]
d=[18, 35 ,87 ,10]
e=[20, 4, 82, 47 ,65]
f=[19, 1, 23, 75, 3, 34]
g=[88, 2, 77, 73, 7, 63, 67]
h=[99, 65, 4 ,28 ,6 ,16 ,70 ,92]
i=[41, 41, 26, 56, 83, 40, 80, 70, 33]
j=[41, 48, 72, 33, 47, 32, 37, 16 ,94, 29]
k=[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
l=[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
m=[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
n=[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
o=[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]


best=0

for b1 in range (0,2):
    totalb = 75 + b[b1]
    for c1 in range (b1,b1+2):
        totalc = totalb + c[c1]
        for d1 in range (c1,c1+2):
            totald = totalc + d[d1]
            for e1 in range (d1,d1+2):
                totale = totald + e[e1]
                for f1 in range (e1,e1+2):
                    totalf = totale + f[f1]
                    for g1 in range (f1,f1+2):
                        totalg = totalf + g[g1]
                        for h1 in range (g1,g1+2):
                            totalh = totalg + h[h1]
                            for i1 in range (h1,h1+2):
                                totali = totalh + i[i1]
                                for j1 in range (i1,i1+2):
                                    totalj = totali + j[j1]
                                    for k1 in range (j1,j1+2):
                                        totalk = totalj + k[k1]
                                        for l1 in range (k1,k1+2):
                                            totall = totalk + l[l1]
                                            for m1 in range (l1,l1+2):
                                                totalm = totall + m[m1]
                                                for n1 in range (m1,m1+2):
                                                    totaln = totalm + n[n1]
                                                    for o1 in range (n1,n1+2):
                                                        totalo = totaln + o[o1]
                                                        if totalo > best:
                                                            best = totalo

print(best)
                                
                                
                        










