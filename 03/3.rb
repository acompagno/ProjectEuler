def isPrime(n)
	if(n < 4) 
		return true
	end
	for i in (3..(n**(0.5)).to_i).step(2)
		if (n % i == 0)
			return false
		end
	end
	return true
end

def main()
	largest  = 0
	number = 600851475143
	for i in (3..(number**(0.5)).to_i).step(2)
		if (isPrime(i) && number%i == 0 && i > largest)
			largest = i
		end
	end
	puts largest
end 

if __FILE__ == $0
	main()
end
