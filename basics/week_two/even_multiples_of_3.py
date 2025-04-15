n = int(input("Enter the number of multiples of 3 from which you want to see even numbers from:"))


found_even = False
if (n < 1):
    print(f"{n}, Value must be greater than 0")
else:
    for i in range(1, n + 1):
        multiple = i * 3
        if (multiple % 2 == 0):
            print(multiple)
            found_even = True
if not found_even:
    print("No even multiple of 3 found")