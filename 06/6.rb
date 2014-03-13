def main()
    sum = square = 0
    for i in 1..100
        sum += i
        square += i*i
    end
    puts (sum*sum)-square
end

if __FILE__ == $0
    main()
end
