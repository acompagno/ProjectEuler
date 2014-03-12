class main  
{
    public static boolean isPalindrome(int n)
    {
        String reversedNum = new StringBuffer(String.valueOf(n)).reverse().toString();
		return n == Integer.valueOf(reversedNum);
    }

    public static void main(String[] args) 
    {
        int i , j , largest = 0;
        for (i = 999 ; i >= 100 ; i--)
		{
            for (j = i ; j >=100 ; j--)
            {
				int temp  = i * j;
                if (isPalindrome(temp) && temp > largest)
                    largest = temp;
            }
        }
        System.out.println("Answer: " + largest);
    }
}
