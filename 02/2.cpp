#include <iostream>
using namespace std;

int main()
{
	long long total = 0 , a = 0 , b = 1 ;
	while(a <= 4000000)
	{
		long long tmp = a + b;
		b = a;
		a = tmp;
		if (a%2 == 0)
			total += a;
	}
	cout << total << "\n";
}
