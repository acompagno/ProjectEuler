#include <stdio.h>

int isDivByRange20(long long n)
{
	long long i;
	for (i = 20 ; i >= 2 ; i--)
	{
		if(n % i != 0)
			return 0;
	}
	return 1;
}

int main()
{
	long long i = 20;
	while (! isDivByRange20(i))
		i += 20;
	printf("%d\n" , i);
}
