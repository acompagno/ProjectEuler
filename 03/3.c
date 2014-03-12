#include <stdio.h>
#include <math.h>

int isPrime(long long n);

int main()
{
	long long i , num = 600851475143 , largest;
	for(i = 3 ; i <= pow(num , 0.5) ; i+=2)
	{
		if (num % i == 0 && isPrime(i))
			largest = i;
	}
	printf("%lld\n" , largest);
}

int isPrime(long long n)
{
	long long i;
	if (n < 4)
		return 1;
	if (n%2 == 0)
		return 0;
	for(i = 3 ; i <= pow(n , 0.5) ; i += 2)
	{
		if(n % i == 0)
			return 0;
	}
	return 1;
}
