#include <stdio.h>

int main ()
{
    long a = 0 , b = 1 , total = 0;
	while (a <= 4000000)
	{
		long tmp = a + b;
		b = a;
		a = tmp;
		if (a % 2 == 0)
			total += a;
	}
	printf("%d\n" , total);
}
