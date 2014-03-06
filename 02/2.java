class main  {
    public static void main(String[] args) {
        int total = 0, i , a =0 , b=1 , current ;
        for (i = 0 ; i < 4000000 ; i++)
        {
            current  = a + b;
            a = b;
            b = current;
            if (current < 4000000 && current %2 == 0)
            {
                total += current;
            }
            if (current >=4000000)
            {
                break;
            }
        }
        System.out.println("Answer: "+total);
    }
}