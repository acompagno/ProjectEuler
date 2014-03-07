def isPrime(x)
	if(x < 4) 
		return true
	end
	for i in (3..(x/2)+1).step(2)
		if (x % i == 0)
			return false
		end
	end
	return true
end

def main()
	largest = 0
	number = 600851475143
	for i in (1..(number**(0.5)).to_i).step(2)
		if (isPrime(i) && number%i == 0 && i > largest)
			largest = i
			puts i
		end
	end
	puts largest
end 

if __FILE__ == $0
	main()
end
