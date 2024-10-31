import os
from logo import logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(logo)
    again = True
    first_number = float(input("What is your first number: "))

    while again:

        operation = input("What's your mathematical operator '+','-','*','/': ")
        second_number = float(input("What is your second number: "))
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        next_operation = input(f"Type 'y' to continue calculating with {result} or 'n' to make a new calculation: ")

        if next_operation == "y":
            first_number = result
        else:
            again = False
            os.system('cls')
            calculator()


calculator()