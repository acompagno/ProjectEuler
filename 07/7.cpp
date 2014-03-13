#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(long long n);

int main()
{
    long long count = 0 , i = 1;
    while (count != 10001)
    {
        if(isPrime(i))
            count ++;
        i += 2;
    }
    cout << i-2 << "\n";
}

bool isPrime(long long n)
{
    if (n < 4)
        return true;
    if (n % 2 == 0)
        return false;
    for (long long i = 3 ; i <= (int)pow(n , 0.5) ; i+=2)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
