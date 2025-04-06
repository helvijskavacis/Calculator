#Creating functions
def add(x,y):
    print("Summed:", x+y)
def subtract(x,y):
    print("Subtracted:", x-y)
def multiply(x,y):
    print("Multiplied:", x*y)
def divide(x,y):
    print("Divided", x/y)

#User instructions and input
print("Enter two numbers to be a part of the equasion")
x = int(input("First number: "))
y = int(input("Second number: "))

#Calling functions
add(x,y)
subtract(x,y)
multiply(x,y)
divide(x,y)