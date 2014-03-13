def main():
    input = open('input.txt').readlines()[0]
    max = 0
    for i in range(len(input) - 4):
        tmp = 1
        for j in list(input[i:i+5]):
            tmp *= int(j)
        if (tmp > max):
            max = tmp
    print(max)

main()
