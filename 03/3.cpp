#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(long long n);

int main()
{
	long long num = 600851475143 , largest;
	for (long long i = 3 ; i <= pow(num , 0.5) ; i+=2)
	{
		if (num % i == 0 && isPrime(i))
			largest = i;
	}
	cout << largest << "\n";
}

bool isPrime(long long n)
{
	if (n < 4)
		return true;
	if (n % 2 == 0)
		return false;
	for(long long i = 3 ; i <= pow(n , 0.5) ; i+=2)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}
