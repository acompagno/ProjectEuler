#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

bool isPalindrome(int n);

int main()
{
	int largest = 0;
	for (int i = 999 ; i >= 100 ; i--)
	{
		for (int j = i ; j >= 100 ; j--)
		{
		int temp = j * i;
		if (temp > largest && isPalindrome(temp))
			largest = temp;
		}
	}
	cout << largest << "\n";
}

bool isPalindrome(int n)
{
	string intStr , intStrRev;
	stringstream ss;
	ss << n;
	intStrRev = intStr = ss.str(); 
	reverse(intStrRev.begin() , intStrRev.end());
	return (intStrRev.compare(intStr) == 0);
}

