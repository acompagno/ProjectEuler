class main  
{
    public static void main(String[] args) 
    {
        int sum = 0 , square = 0;
        for (int i = 1 ; i <= 100 ; i++)
        {
            sum += i;
            square += i*i;
        }
        System.out.println("Answer: "+ ((sum*sum) - square));
    }
}
