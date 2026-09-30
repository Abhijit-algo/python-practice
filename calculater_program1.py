# 1. Ask the user to choose an operation
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
choice = input("Choose operation (1, 2, 3, or 4): ")

# 2. Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 3. Calculate based on the user's choice
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    print("Result:", num1 / num2)
else:
    print("Invalid Choice!")
