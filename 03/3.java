import java.math.BigInteger;

class main
{
    public static void main(String[] args) 
    {          
        BigInteger num = new BigInteger("600851475143");
		BigInteger largest = new BigInteger("0");
		for (BigInteger i = BigInteger.valueOf(3) ; i.compareTo(sqrt(num)) < 0 ; i=i.add(BigInteger.valueOf(2)))
		{
			if (num.mod(i).equals(BigInteger.ZERO) && isPrime(i))
				largest = i;
		}
		System.out.println("" + largest);
    }

	public static boolean isPrime(BigInteger n)
	{
		if (n.compareTo(BigInteger.valueOf(4)) < 0)
			return true;
		if (n.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO))
			return false;
		for (BigInteger i = BigInteger.valueOf(3) ; i.compareTo(sqrt(n)) < 0 ; i=i.add(BigInteger.ONE))
		{
			if (n.mod(i).equals(BigInteger.ZERO))
				return false;
		}
		return true;
	}

	public static BigInteger sqrt(BigInteger n) 
	{
		BigInteger a = BigInteger.ONE;
	    BigInteger b = new BigInteger(n.shiftRight(5).add(new BigInteger("8")).toString());
		while(b.compareTo(a) >= 0) 
		{
			BigInteger mid = new BigInteger(a.add(b).shiftRight(1).toString());
			if(mid.multiply(mid).compareTo(n) > 0) 
				b = mid.subtract(BigInteger.ONE);
			else 
				a = mid.add(BigInteger.ONE);
		}
		return a.subtract(BigInteger.ONE);
	}
}
