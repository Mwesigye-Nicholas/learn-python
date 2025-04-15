n = int(input("Enter the number of even multiples of 3 you want to see: "))
start = int(input("Please enter the starting point: "))
end = int(input("Please enter the ending point: "))
step = int(input("Please enter the value by which you want the increment to happen: "))

found_even = False
number_of_evens = 0;

if (n < 1):
    print(f"{n}, Please enter the value of n greater than 0")
else:
    for i in range(start, end + 1, step):
        multiple = i * 3
        if (multiple % 2 == 0):
            print(multiple)
            found_even = True
            number_of_evens += 1
            if (number_of_evens >= n):
                break
if not found_even:
    print("No even number found in the range")