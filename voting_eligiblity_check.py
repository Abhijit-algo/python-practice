# 1. Ask the user for their age
age_input = input("Enter your age: ")

# 2. Convert the text input into a whole number (integer)
age = int(age_input)

# 3. Check if the age is 18 or older
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are too young to vote.")
