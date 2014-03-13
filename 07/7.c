#include <stdio.h>
#include <math.h>

int isPrime(long long n);

int main()
{
    long long  i = 1 , count = 0;
    while (count != 10001)
    {
        if(isPrime(i))
            count ++;
        i += 2;
    }
    printf("%lld\n" , i-2);
}

int isPrime(long long n)
{
    long long i;
    if (n < 4 )
        return 1;
    if (n%2 == 0)
        return 0;
    for(i = 3 ; i <= pow(n , 0.5) ; i+=2)
    {  
        if (n % i == 0)
            return 0;
    }
    return 1 ;
}
