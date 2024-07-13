#simple function

def greet():
    print("hello world")

#Function with parameter

def add(a,b):
    return a+b

#function with default parameter

def square(x=1):
    return x*x

#function with variable length arguments

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

def printInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

greet()
print("Result of addition:",add(2,4))
print("square of number is: ",square())
print("Total : ",sum(1,2,2,4,5,))
printInfo(name="roy",age=12)
