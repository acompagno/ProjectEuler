def main()
	largest = 0
	for i in 999.downto(100)
		for a in i.downto(100)
			tmp = a * i
			if ("#{tmp}".reverse == "#{tmp}" && tmp > largest )
				largest  = tmp
				break
			end
		end
	end
	puts largest
end

if __FILE__ == $0
	main()
end
