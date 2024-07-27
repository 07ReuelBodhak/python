# Encapsulation and Abstraction

Both encapsulation and data hiding are the concept of OOP

### 1. Encapsulation

_Definition:_
Encapsulation is the building of data(variables) and methods(functions) that operate on data into a single unit or a class. it restricts direct access to some of an objects components, which is a means of preventing accidental interference and misuse of data.

_why Encapsulation?_

- **Data Hiding**: Encapsulation helps to hide data the internal state of the object and only expose a controlled interface

- **Modularity**: It allows the code to be more modular and organized.

- **Maintenance**: It makes the code easier to maintain and modify.

### How to Implement Encapsulation in Python:

In Python, encapsulation is achieved using access modifiers:

- Public: Accessible from anywhere.

- Protected: Prefix with a single underscore \_
  (convention, not enforced).

- Private: Prefix with a double underscore \_\_.

```python
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand  # public variable
        self._color = color  # protected variable (convention)
        self.__year = year  # private variable (name-mangled to _Car__year)

    def displayInfo(self):
        print(f"Brand : {self.brand}\nColor : {self._color}\nYear : {self.__year}")

    def changeYear(self, yr):
        self.__year = yr

C = Car("Toyota", "Red", 2016)
C.displayInfo()
print()

# Modifying public and protected variables directly
C.brand = "Audi"
# C.__year = 2018  # This will give an error due to name mangling
C.changeYear(2015)
C.displayInfo()

```

### 2. Abstraction

_Definition_:
Abstraction is the concept of hiding the complex implementation detail showing only the essential features of the object. Its about creating simple interface to interact with the complex systems.

_why Abstraction?_

- **Simplification**: It simplifies the use of complex systems by providing a simplified interface.

- **Focus on Essentials**: It allows the user to focus on the essential aspects without worrying about the intricate details.

- **Reusability**: Abstract classes and interfaces can be reused across different programs.

### How to Implement Abstraction in Python:

In Python, abstraction is implemented using abstract classes and interfaces. Python provides the abc module to implement abstraction.

```python
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        return "bark"

class Cat(Animal):
    def makeSound(self):
        return "meow"

c = Cat()
print(c.makeSound())

D = Dog()
print(D.makeSound())
```
