class main 
{
    public static void main(String[] args) 
	{
        int total = 0 , a = 0 , b = 1;
		while (a <= 4000000)
		{
			int tmp = a + b;
			b = a;
			a = tmp;
			if (a % 2 == 0)
				total += a;
		}
        System.out.println("Answer: "+total);
    }
}
