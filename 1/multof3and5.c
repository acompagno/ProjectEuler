#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
    int i , z =0 ;
    for(i=0 ; i < 1000 ; i++)
    {
        if(i%3==0 || i%5==0)
        {
            z=z+i;
        }
    }
    printf("%d",z);
}
