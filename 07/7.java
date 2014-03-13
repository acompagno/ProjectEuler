class main
{
    public static void main (String[] args)
    {
        int i = 1 , count = 0;
        while (count != 10001)
        {
            if (isPrime(i))
                count++;
            i += 2;
        }
        System.out.println("" + (i-2));
    }
    public static boolean isPrime(int n)
    {
        if (n < 4)
            return true;
        if (n % 2 == 0)
            return false;
        for (int i = 3 ; i <= (int)Math.pow(n , 0.5) ; i += 2)
        {
            if (n%i == 0)
                return false;
        }
        return true;
    }
}
