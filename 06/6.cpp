#include <iostream>

using namespace std;

int main()
{
	long long sum = 0 , square = 0;
	for (int i = 1 ; i <= 100 ; i++)
	{
		sum += i;
		square += i * i;
	}
	cout << (sum * sum - square);
	cout << "\n";
}
