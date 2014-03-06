class main  {
    public static void main(String[] args) 
    {
        int i , sum = 0 , square = 0;
        for (i = 1 ; i <=100 ; i++)
        {
            sum += i;
            square += i*i;
        }
        System.out.println("Answer: "+((sum*sum) - square));
    }
}