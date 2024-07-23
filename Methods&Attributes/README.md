# Methods And Attributes

## Attributes

Attributes are variables that belongs to an object or a class. They are used to store data about the object. There are two types of attributes

1. Instance Attributes: These are specific to an instance of a class. They are usually defined within the **init** method of the class.

2. Class Attributes: These are shared by all instances of the class. They are defined within the class but outside any instance methods.

```python
class Car:
    wheels = 4

    def __init__(self, color):
        self.color = color

c = Car("black")
print(c.wheels)
print(c.color)
```

## Methods

Methods are functions defined within a class that describe the behaviors of an object. They operate on the attributes of the object.

### Instance Methods

Instance methods are the most common type of method in a class. They operate on an instance of the class (an object) and can access and modify the object's attributes. They take self as their first parameter, which is a reference to the instance calling the method.

**Syntax**:

```python
    class Exp:
        def instance_Method(self,arg1,arg2):
            pass
```

### Class Methods

Class methods are used to access or modify the class state that applies to all instances of the class. They are defined using the @classmethod decorator and take cls as their first parameter, which is a reference to the class itself. This allows class methods to modify class-level attributes.

**Syntax:**

```python
class Exp:
    @classmethod
    def class_method(cls,arg1,arg2):
        pass
```

### Static Method

Static methods do not operate on an instance or a class; they are independent and do not take self or cls as their first parameter. They are defined using the @staticmethod decorator. Static methods behave like regular functions but belong to the class's namespace

**Syntax:**

```python
class Exp:
    @staticmethod
    def static_method(args):
        pass
```
