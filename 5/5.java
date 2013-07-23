class main  {
    public static boolean is1to20div(int n)
    {
        int i;
        for (i=1 ; i <= 20 ; i++)
        {
            if(n%i != 0)
            {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) 
    {
        int i = 1;
        while (true)
        {
            if (is1to20div(i))
            {
                System.out.println("Answer: "+i);
                break;
            }
            i++;
        }
    }
}