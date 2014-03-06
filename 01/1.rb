def main
	count = 0
	for i in 1..999
		if i%3 == 0 || i%5 == 0 then
			count += i
		end
	end
	puts count
end

if __FILE__ == $0
	main
end
