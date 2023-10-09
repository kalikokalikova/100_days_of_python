# Calculator program
def add_numbers(a,b):
    return a+b

def subtract_numbers(a,b):
    return a-b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b): #TODO check for zero
    return a/b

operations = {
            "+": add_numbers,
            "-": subtract_numbers,
            "*": multiply_numbers,
            "/": divide_numbers
        }

def calculator():
    result = 0
    continue_calculation = True
    first_number = float(input("What's the first number? "))

    while continue_calculation:
        operator = input("Pick an operation: (+, -, *, or /) ")
        next_number = float(input("What's the next number? "))
        if operator == '/' and next_number == 0:
            print("Don't be a jerk. You'll break my calculator.")
            continue
        operation = operations[operator]
        result = operation(first_number, next_number)

        if input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ") == "y":
            first_number = result
        else:
            continue_calculation = False
            calculator()

calculator()




