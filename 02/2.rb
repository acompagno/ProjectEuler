def main
	a , b , total = 0 , 1 , 0
	while a <= 4000000 do 
		tmp = a + b
		b = a
		a  = tmp
		if a % 2 == 0 
			total += a
		end
	end
	puts total
end

if __FILE__ == $0
	main
end
