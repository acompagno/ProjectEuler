def isPrime(x)
	if(x < 4) 
		return true
	end
	for i in 2..(x/2)
		if (x % i == 0)
			return false
		end
	end
	return true
end

def main()
	largest = 0
	loopLimit = 600851475143**(0.5)
	for i in 1..loopLimit.to_i
		if (isPrime(i) && 600851475143%i == 0 && i > largest)
			largest = i
			puts i
		end
	end
	puts i
end 

if __FILE__ == $0
	main()
end
