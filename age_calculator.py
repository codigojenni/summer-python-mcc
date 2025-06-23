# Ask for user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Ask for current year and birth year, convert to integers
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year

# Greet the user and tell them their age (using string concatenation + newline)
print("Hello, " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old this year.")

# Increase age by 1 
age += 1

# Print how old the user will be next year using an f-string
print(f"Next year, you will be {age} years old in the year {current_year + 1}.")

# Completion statement
print("Completed by, Jennifer Mendoza Trejo")
