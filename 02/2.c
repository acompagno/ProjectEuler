#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
    int a =0,i , b=1, c , z = 0 ;
    printf ("%d\n %d\n",a,b);

        for (i = 0 ; i < 300 ; i++)
        {
            c = a + b;
            a = b;
            b = c;
            printf("%d\n",c);

            if (c%2==0 && c < 4000000)
            {
               z = z +c ;
            }
            if (c >= 4000000)
            {
                printf("z=%d",z);
                break;
            }


        }
   // printf("%d",z);
}
