#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
    int a , b , c=0 , d , i , z , array[10000000]={0};
    for(a = 2 ; a <= 100 ; a++)
    {
        for(b = 2 ; b <= 100 ; b++)
        {
            d = pow(a,b);
            z=0;
            for(i = 0 ; i < c ; i++)
            {
                if(array[i] == d)
                {
                    z++;
                }
            }
            if(z==0)
            {
                array[c]=d;
                c++;
            }
        }
    }
    printf("%d",c);
}
