#2.Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print("Result =", result)

elif operator == '-':
    result = num1 - num2
    print("Result =", result)

elif operator == '*':
    result = num1 * num2
    print("Result =", result)

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")
