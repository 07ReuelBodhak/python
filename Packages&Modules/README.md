# Packages and Modules

## Module

A module is a single file(with a .py extension) that contains python code. It can define functions, classes, and variables. It can also include runnable code. Modules help in organizing Python code into manageable and reusable components.

1. Creating a Module :

   to create a module, simply save a python file with any name you like. for example lets create a module name myModule.py

   ```python
   # myModule.py

   def greet(name):
       print(f"hello {name}")

   class person:
       def __init__(self,name):
           self.name = name

       def introduce(self):
           print(f"hello i am {self.name}")
   ```

2. Importing a module

   You can use the import statement to import the module into another Python file or an interactive session. For example:

   ```python
    import myModule

    myModule.greet("alex")

    p = myModule.Person("bob")
    p.introduce()
   ```

## Package

A package is a way of organizing related modules into a directory hierarchy. A package must contain a special file named **init**.py, which can be empty or contain initialization code for the package.

1. Creating a Package

   To create a package, create a directory and add the **init**.py file along with the module files. For example:

   ```markdown
   mypackage/
   **init**.py
   module1.py
   module2.py
   ```
