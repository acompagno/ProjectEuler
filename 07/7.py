def main():
     i = 1
     count = 0
     while (count != 10001):
         if (isPrime(i)):
             count = count + 1
         i = i + 2
     print (i - 2)

def isPrime(n):
    if (n < 4):
        return True
    if (n % 2 == 0):
        return False
    for i in range(3 , int((n**0.5) + 1)  , 2):
        if (n % i == 0):
            return False
    return True

main()
