def main()
    i = 1
    count = 0
    while (count != 10001)
        if (isPrime(i))
            count += 1
        end
        i += 2
    end
    puts i-2
end 

def isPrime(n)
    if (n < 4)
        return true
    end
    if (n % 2 == 0)
        return false
    end
    for i in (3..n**0.5).step(2)
        if (n % i == 0)
            return false
        end
    end
    return true
end

if __FILE__ == $0
    main()
end
