# Special Methods

Special method in python is also known as magic method or dunder (double underscore) methods, are methods that have double underscores at the beginning and end of their names. These methods allow you to define how objects of your custom classes behave with built-in functions and operators.

## Initialization and Representation

1. **`__init__(self,...)`**: this is the initializer method, commonly known as the constructor. It is called when an object is created from a class, and it allows the class to initialize the attributes of the object.

   ```python
   class Person:
       def __init__(self,name,age):
           self.name = name
           self.age = age
   ```

2. **`__str__(self)`**: This method is called by the str() function and the print function to get a readable string representation of an object.

   ```python
    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name}, {self.age} years old"

    p = Person("alex",56)
    print(p)
   ```

3. **`__repr__(self)`** : This method is called by the repr() function and is supposed to return an unambiguous string representation of the object, often one that can be used to recreate the object

   ```python
    class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

    p = Person("alex",56)
    print(repr(p))

   ```

## Arithmetic Operations

4. **`__add__(self,other)`** : This method is used to define the behavior of the + operator.

   - self: The left operand in the addition.
   - other: The right operand in the addition.

   ```python
   class Vector:
   def __init__(self,x,y):
       self.x = x
       self.y = y

   def __add__(self,other):
       return Vector(self.x + other.x, self.y + other.y)

   def __repr__(self):
       return f'Vector({self.x}, {self.y})'

   v1 = Vector(3,5)
   v2 = Vector(6,7)
   print(v1 + v2)
   ```

5. **`__sub__(self, other)`**: This method is used to define the behavior of the - operator.

   - self: The left operand in the addition.

   - other: The right operand in the addition.

   ```python
    class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

   ```

6. **`__mul__(self,other)`** : this method is used to define the behavior of the '\*' operator.

   ```python
    class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self,other):
        return Vector(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    v1 = Vector(2,4)
    v2 = Vector(4,5)
    print(v1 * v2)

   ```

## Comparison Operations

7. **`__eq__(self,other)`**: This method is used to define the behavior of the == operator.

   ```python
    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        return self.name == other.name

    p1 = Person("roy",12)
    p2 = Person("roy",23)
    print(p1 == p2)

   ```

8. **`__lt__(self,other)`** : this method is used to define the behavior of the '<'(less than) operator.

   ```python
    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    p1 = Person("roy",12)
    p2 = Person("roy",23)
    print(p1 <  p2)

   ```

## Container Emulation

9. **`__len__(self)`**: this method is called by the 'len()' function to get the length of an object.

   ```python
    class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    my_list = MyList([1,2,3,4,5])
    print(len(my_list))
   ```

10. **`__getitem(self,key)__`**: This method is used to define the behavior of indexing(`obj[key]`).

    ```python
    class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self,index):
        return self.items[index]

    my_list = MyList([1,2,3,4,5])
    print(len(my_list))
    print(my_list[0])

    ```

## Attribute Access

11. **`__getattr__(self,name)`** : This method is called when trying to access an attribute that does not exists on an object

    ```python
    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self,name):
        return f'{name} attribute does not exists'

    p = Person('Alice', 23)
    print(p.height)
    print(p.age)
    ```

## Object Destruction

12. **`__del__(self)`** : This Method is called when an object is about to be destroyed. It is the destruction method.

    ```python
    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} has been deleted")

    p = Person("alex",36)
    del p

    ```

## Callable object

13. **`__call__(self, *args, *kwargs)`** : This method allows an object to be called as a function.

    ```python
    class Multiplier:
    def __init__(self,value):
        self.value = value

    def __call__(self,x):
        return self.value * x

    m = Multiplier(3)
    print(m(3))
    ```
