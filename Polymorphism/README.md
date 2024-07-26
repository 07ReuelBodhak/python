# Polymorphism

Polymorphism is a core concept in object-oriented programming that allows object of different classes to be treated as objects of a common superclass. it provides a way to perform a single action in different forms. In Python, polymorphism allows you to define methods in the child class with the same name as defined in their parent class. Here are the key aspects of polymorphism in Python:

## 1. Method Overriding

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass, The overridden method in the subclass should have the same name, parameter, and return type as the method in the parent class

```python
class Animal:
    def sound(self):
        print("animal makes sound")

class Cat(Animal):
    def sound(self):
        print("cat meows")

c = Cat()
c.sound()
```

## 2. Method Overloading

Python does not support method overloading by default as in other languages like java or C++, however you can achieve similar behavior by using default arguments or variable-lengths

```python

class MathOperation:
    ##default argument
    def add(self,a,b,c=0):
        return a + b + c

    ## Variable-length ars
    def sum(self,*nums):
        sum = 0
        for i in nums:
            sum += i
        return sum
m = MathOperation()
print(m.add(1,2,5))
print(m.add(1,2))
print(m.sum(1,2,3,4,5,6))
print(m.sum(1,2,3,4,5))
```

## 3. Polymorphism with function and objects

Polymorphism can also be implemented using function ans objects. this allows function to use objects of different types and invoke methods that are common to all these objects

```python
class Bird:
    def fly(self):
        return "Flying"

class Airplane:
    def fly(self):
        return "Flying in the Sky"

def take_off(entity):
    print(entity.fly())

Bird = Bird()
Airplane = Airplane()
take_off(Bird)
take_off(Airplane)
```

## 4. Polymorphism through inheritance

Through Inheritance, a child class can inherit methods and properties of the parent class. When the child class needs to provide a specific implementation for a method already provided by the parent class, it overrides that method.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

R = Rectangle(32,54)
print(R.area())

C = Circle(45)
print(C.area())
```
