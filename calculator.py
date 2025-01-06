# Simple calculator program

print("Welcome to the simple calculator!")

# Asking the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking the user to choose an operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter the number of your choice (1/2/3/4): ")

# Performing the selected operation
if choice == "1":
    result = num1 + num2
    print("The result of addition is:", result)
elif choice == "2":
    result = num1 - num2
    print("The result of subtraction is:", result)
elif choice == "3":
    result = num1 * num2
    print("The result of multiplication is:", result)
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid choice. Please restart the program and try again.")

print("Thank you for using the calculator!")
