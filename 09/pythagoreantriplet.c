#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
    int a , b , c , i ;

    for(b=0 ; b < 1000  ; b++ )
    {
        for(a = 0 ; a < 1000-b ; a++)
        {
            c = 1000 - a - b ;
            if (pow(a,2)+ pow(b,2) == pow(c,2) && c>b && b>a )
            {
                i = a*b*c;
                printf("a =%d b =%d c =%d\n",a,b,c);
                printf("abc = %d",i);
            }
        }
    }
}

