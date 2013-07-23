class main  {
    public static boolean ispalindrome(int n)
    {
        String temp = new StringBuffer(String.valueOf(n)).reverse().toString();
        if (n==Integer.valueOf(temp))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public static void main(String[] args) 
    {
        int i,b , best = 0;
        for (i = 999 ;i >= 100 ; i--)
        {
            for (b = 999 ; b >=100; b--)
            {
                if (ispalindrome(i*b) && i*b>best)
                {
                    best = i*b;
                }
            }
        }
        System.out.println("Answer: "+best);
    }
}