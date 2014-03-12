#include <stdio.h>

int main()
{
	long long i , sum = 0 , square = 0;
	for (i = 1 ; i <= 100 ; i++)
	{
		sum += i;
		square += i * i;
	}
	printf("%lld\n" , (sum * sum) - square);
}
