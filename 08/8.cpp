#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int max = 0;
    string input;
    ifstream inputFile( "input.txt" );
    inputFile >> input;
    for (int i = 0 ; i < input.length() - 5 ; i++)
    {
        int tmp = 1;
        for (int j = i ; j < i+5 ; j++)
            tmp *= (int)input.at(j)-48;
        max = (tmp > max) ? tmp : max ;
    }
    cout << max << "\n";

}
