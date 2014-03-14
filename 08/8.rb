def main()
    max = 0
    input = File.open("input.txt" , "r").read
    for i in 1..input.length()-5
        tmp = 1
        for j in i..i+4
            tmp *= input[j].ord - 48
        end
        max = tmp > max ? tmp : max
    end
    puts max
end

if __FILE__ == $0
    main()
end
