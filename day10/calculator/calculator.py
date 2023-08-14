import os
from calculator_art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
}

def calculator():
    print(logo)
    is_end = False

    num1 = float(input("What's the first number?: "))

    for i in operators:
        print(i)

    while not is_end:
        op = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        result = operators[op](num1, num2)

        print(f"{num1} {op} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            os.system("clear")
            is_end = True
            calculator()


calculator()

# while True:
#     calculator()