def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for the operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        return

    # Get user input for the numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the selected operation
    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = '/'

    # Print the result in a readable format
    print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()