def main()
	i = 20
	while (! isDivByRange20(i))
		i += 20
	end
	puts i
end

def isDivByRange20(n)
	for i in 20.downto(2)
		if (n % i != 0)
			return false
		end
	end
	return true
end

if __FILE__ == $0
	main()
end
