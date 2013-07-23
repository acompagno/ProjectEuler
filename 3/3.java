
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
        int current = 0, i;
        for(i = 0 ; i < int(600851475143/2) ; i = i +2)
        {
            if (600851475143%i == 0 && isprime(i))
            {
                current = i;
            }
        }            
        System.out.println("Answer:"+current);
    }
}