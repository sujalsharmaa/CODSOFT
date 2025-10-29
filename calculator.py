# Simple Calculator Program

# Prompt user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user's choice
choice = input("\nEnter your choice (1/2/3/4): ")

# Perform calculation based on user's choice
if choice == '1' or choice == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2' or choice == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3' or choice == '*':
    result = num1 * num2
    print(f"\nResult: {num1} × {num2} = {result}")
elif choice == '4' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} ÷ {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid choice! Please select a valid operation.")
