#include <iostream>

using namespace std;

bool isDivByRange20(long long n);

int main()
{
	long long i = 20;
	while (! isDivByRange20(i))
		i += 20;
	cout << i << "\n";
}

bool isDivByRange20(long long n)
{
	for (int i = 20 ; i >= 2 ; i--)
	{
		if (n % i != 0)
			return false;
	}
	return true;
}
