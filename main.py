import math
#Math functions
def add(x,y): return x+y
def subtract(x,y): return x-y
def multiply(x,y): return x*y
def divide(x,y): 
    try:
         return x/y
    except ZeroDivisionError:
         print("Can't divide by zero!")
         return None
def exponentiation(x,y):
    try:
         return x**y
    except ZeroDivisionError:
         print("Can't perform exponention of 0 by a negative power.")
         return None
def square_root(x):
    if x < 0:
        return f"Can't calculate sqrt({x}), as it must be positive!"
    return math.sqrt(x)

#see history
def history():
    while True: 
        input_history = input("Would you like to see the calculation history? y/n")
        if input_history == "y":
            with open("Calculations.txt", "r") as file:
                for line in file:
                    print(line.strip())
                break
        elif input_history == "n":
            print("Thank you for using the calculator!")
            break
        else: 
            print("Oops, try again: ")

#User inserts variable
def user_variable():
    while True:
        try:
            variable = int(input("Variable: "))
            return variable
        except ValueError:
            print("Please, re-enter an integer: ")

#User inserts operator
def user_operator():
    while True:
        operator = input("Choose operator: ( +; -; *; /; **; sqrt; = )")
        if operator in ["+", "-", "*", "/", "**", "sqrt", "="]: #check if operator is correct format
            return operator
        else:
            print("Please re-enter a valid operator: ")

#Writing user input in the list
def write_in_list():
    calc_list = []
    while True:
        calc_list.append(user_variable())
        operator_type = user_operator()
        calc_list.append(operator_type)
        if operator_type == "=" or operator_type == "sqrt":
            break
    return calc_list


def calculate_list(calc_list):
    counter = -1
    total = calc_list[0]
    for var in calc_list[2::2]:
        counter += 2
        if calc_list[counter] == "+":
            total = add(total, var)
        elif calc_list[counter] == "-":
            total = subtract(total, var)
        elif calc_list[counter] == "*":
            total = multiply(total, var)
        elif calc_list[counter] == "/":
            total = divide(total, var)
        elif calc_list[counter] == "**":
            total = total ** var
        elif calc_list[counter] == "sqrt":
            total = square_root(total)
            break
        else: # when it's (=)
            break
    calc_list.append(total)
    with open("Calculations.txt", "a") as file:
        file.write(f"\n{" ".join(map(str, calc_list))}")
    print(' '.join(map(str, calc_list)))

calculate_list(write_in_list())
history()