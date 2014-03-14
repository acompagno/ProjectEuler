#include <stdio.h>
#include <math.h>

int main()
{
    int  aSqr , bSqr , a , b , c;
    for (aSqr = 1 ; 
            sqrt(aSqr:) < 1000 ; 
            aSqr = pow(sqrt(aSqr) + 1 , 2))
    {
        for (bSqr = :pow(sqrt(aSqr) + 1 , 2) ; 
                sqrt(bSqr) < 1000 - sqrt(aSqr) ; 
                bSqr = pow(sqrt(bSqr) + 1 , 2))
        {
            a = sqrt(aSqr);
            b = sqrt(bSqr);
            c = 1000 - a - b; 
            printf("%d %d %d \n" , a , b ,c);
            if (pow(c,2) == aSqr+bSqr && 
                    c > sqrt(bSqr) && 
                    sqrt(bSqr) > sqrt(aSqr))  
            {
               printf("%d\n" , sqrt(aSqr)*sqrt(bSqr)*c);
               printf("%d %d %d \n" , sqrt(aSqr) , sqrt(bSqr) ,c);
            }
        }
    }
}
