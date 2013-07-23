class main  {
    public static boolean isprime(int n)
    {
        int i;
        if (n < 2)
        {
            return false ;
        }
        else if (n == 2)
        {
            return true ;
        }
        else if (n % 2 == 0)
        {
            return false ;
        }
        else
        {
            for(i = 3 ; i < (int)(Math.sqrt(n))+2 ; i=i+2)
            {
                if (n%i == 0)
                {
                    return false;
                }
            } 
            return true;
        }
    }

    public static void main(String[] args) 
    {
        int i = 1 ,count = 0;
        while (true)
        {
            if (isprime(i))
            {
                count++;
                if(count == 10001)
                {
                    System.out.println("Answer: "+i);
                    break;
                }
            }
            i++;
        }
    }
}