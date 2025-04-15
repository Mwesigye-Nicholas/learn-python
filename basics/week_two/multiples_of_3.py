n = int(input("The number of multiples of 3 to print: "))

if (n < 1):
    print(f"{n} the value of n should be one or greater")
else:
    for i in range(1, n + 1):
        print(i * 3)