#include <stdio.h>
#include <string.h>
int main()
{
    char input[1001];
    FILE *inputFile = fopen("input.txt" , "r");
    fscanf(inputFile , "%s" , &input) ;
    int inputLength = strlen(input) , max = 0 , i , j;
    for (i = 0 ; i <= inputLength - 5 ; i++)
    {
        int tmp = 1;
        for (j = i ; j < i + 5 ; j++)
            tmp *= (int)input[j]-48;
        if (tmp > max)
            max = tmp;
    }
    printf("%d\n" , max);
}
