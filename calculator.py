import math

#Creating math functions
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
        return f"Can't calculate Sqrt({x}), as it must be positive!"
    return math.sqrt(x)

#User input functions
def user_input():
    try:
        x = int(input("Insert X value: "))
        y = int(input("Insert Y value: "))
        return x,y
    except ValueError: 
        print ("Make sure to enter numbers rather than strings!")
        return user_input()        

#"Mothership" function
def calculations(x,y):
    print(f"{x} + {y} = ", add(x,y))
    print(f"{x} - {y} = ", subtract(x,y))
    print(f"{x} * {y} = ", multiply(x,y))
    print(f"{x} / {y} = ", divide(x,y))
    print(f"{x} ** {y} = ", exponentiation(x,y))
    print(f"Sqrt({x}) = ", square_root(x))
    print(f"Sqrt({y}) = ", square_root(y))   
            
#Run the code
x,y = user_input()
calculations(x,y)


    