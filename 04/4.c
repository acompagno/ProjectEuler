#include <stdio.h>
#include <string.h>

int isPalindrome(int n);
void *reverseString(char *str);

int main ()
{
    int i , j , largest = 0;
	for (i = 999 ; i >= 100 ; i--)
	{
		for (j = i ; j >= 100 ; j--)
		{
			int temp = j * i;
			if (isPalindrome(temp) && temp > largest)
				largest = temp;	
		}
	}
	printf("%d\n" , largest);
}

int isPalindrome(int n)
{
	char intStr[7] , intStrRev[7];
	sprintf(intStr , "%d", n);
	sprintf(intStrRev , "%s" , intStr);
	reverseString(intStrRev);
	if (strcmp(intStrRev , intStr) == 0)
		return 1;
	else 
		return 0;
}

/*
*Reverse string function from the url below
*http://www8.cs.umu.se/~isak/snippets/strrev.c
*/
void *reverseString(char *str)
{
	char *p1, *p2;
	if (! str || ! *str)
		return str;
	for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
	{
		*p1 ^= *p2;
		*p2 ^= *p1;
		*p1 ^= *p2;
	}
	return str;
}
