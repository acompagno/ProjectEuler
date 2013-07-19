#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
    int i , b , c , num, array[6] = {0};

    for (i = 1000 ; i>100 ; i--)
    {
        for (b = 1000 ; b>100 ; b--)
        {
            c = i * b ;
            num = c ;
            while(num>0)
            {
               array[i--] = num%10;
               num /=10;
            }
            if ( array[5] == array[0] && array[4]==array[1] && array[3]==array[2])
            {
                printf("%d",c);
                break;
            }
        }
    }
}
