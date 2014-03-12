class main  
{
    public static boolean isDivByRange20(int n)
    {
        for (int i = 20 ; i >= 2 ; i--)
        {
            if(n%i != 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) 
    {
		int i = 20;
		while (! isDivByRange20(i))
			i += 20;
		System.out.println(""+i);
    }
}
