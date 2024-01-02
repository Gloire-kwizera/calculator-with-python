print("Simple Calculator")
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
operator = input("Choose an operator (+, -, *, /): ")

try:
    num1 = float(number1)
    num2 = float(number2)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operator.")
    
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers.")
