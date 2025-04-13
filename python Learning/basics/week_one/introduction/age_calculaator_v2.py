try:
    birth_year = int(input("Please enter your year of birth: "))
    current_year = 2025
    age = current_year - birth_year
    print(f"You are {age} years old.")
except ValueError:
    print("Oops, please year of birth should be a number")