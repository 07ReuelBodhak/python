# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). In Python, inheritance enables you to create a new class that is a modified version of an existing class, promoting code reuse and logical structuring of code.

### Basic syntax

```python
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
```

### Key Concept of inheritance

1. **Single Inheritance**

   This is the simple form of inheritance when child class inherit from single parent class

   ```python
    class Parent:
        def method_parent(self):
            print("parent method called")

    class Child(Parent):
        def child_method(self):
            print("child method called")

    c = Child()
    c.method_parent()
    c.child_method()
   ```

2. **Multiple Inheritance**

   A class can inherit from more than one parent class

   ```python
    class Parent1:
    def parent1_method(self):
        print("parent 1")

    class Parent2:
        def parent2_method(self):
            print("parent 2")

    class Child(Parent1,Parent2):
        def child_method(self):
            print("child method called")

    c = Child()
    c.parent1_method()
    c.parent2_method()
    c.child_method()
   ```

3. **Overriding Methods:**

   Child classes can override methods from the parent class to provide a specific implementation.

   ```python
    class Parent:
    def greet(self):
        print("greetings by child")

    class Child(Parent):
        def greet(self):
            print("greeting by child")

    c = Child()
    c.greet()
   ```

4. **The super() Function**

   The super() function allows you to call methods from the parent class, facilitating the reuse of code from the parent class in the child class.

   ```python
   class Parent:
   def __init__(self,name):
       self.name = name

   def calculateAge(self,yr):
       return 2024 - yr

   class Child(Parent):
       def __init__(self,name,born):
           super().__init__(name)
           self.born =born

       def greet(self):
           print(f"hii my name is {self.name}, and my age is {self.calculateAge(self.born)}")

   c = Child("ace", 1998)
   c.greet()

   ```

5. **Inheritance Hierarchy**

   Inheritance can be extended across multiple levels, forming an inheritance hierarchy.

   ```python
   class GrandParent:
   def method_grandParent(self):
       print("hello from grand parent")

   class Parent(GrandParent):
       def method_Parent(self):
           print("hello from parent")

   class Child(Parent):
       def method_child(self):
           print("hello from child")

   c = Child()
   c.method_grandParent()
   c.method_Parent()
   c.method_child()
   ```
