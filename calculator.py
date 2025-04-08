#Creating functions
def add(x,y): return x+y
def subtract(x,y): return x-y
def multiply(x,y): return x*y
def divide(x,y): 
    return x/y if y != 0 else "Cannot divide by zero!"

x = 5
y = 6
#Calling functions
print(f"{x} + {y} = ", add(x,y))
print(f"{x} - {y} = ", subtract(x,y))
print(f"{x} * {y} = ", multiply(x,y))
print(f"{x} / {y} = ", divide(x,y))