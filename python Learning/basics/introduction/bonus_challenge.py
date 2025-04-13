try:
   current_year = 2025
   year_of_birth = int(input("Please enter your year of birth: "))
   age = current_year - year_of_birth
   if year_of_birth < 2022:
       age = 2022 - year_of_birth
       print(f"You turned {age} years old in 2022");
   elif (year_of_birth > 2022 and year_of_birth < 2025):
       age = 2025 - year_of_birth
       print(f"You turned {age} years old in 2025 ")
   else:
       print(f"You have provided a future year of birth")
       
except ValueError:
    print(f"Oops!, the year of birth should be a number")