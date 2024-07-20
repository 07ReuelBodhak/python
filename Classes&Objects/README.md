# Classes And Objects

## Classes

A class is an blueprint of an object. it defines a set of attributes and methods that the created object will have

- Attributes (Properties): Variables that store data specific to the class and its objects.

- Methods (Functions): Functions that define the behaviors or actions that objects of the class can perform.

### Defining a class

To define a class in Python, you use the class keyword followed by the class name and a colon. By convention, class names are written in CamelCase.

```python
class ClassName:
    #class Attributes
    #class methods
```

## Objects

An object is an instance of an class. It is created from the class blueprint and u can use the attributes and methods defined in the class

### creating object

To create an object, you call the class as if it were a function, passing the necessary arguments to the constructor method.

```python
my_car = Car("red","toyota","corolla")
```

### Accessing Attributes of an class

You can access the attributes and methods of an object using dot notation.

```python
print(my_car.brand)
print(my_car.color)
```
