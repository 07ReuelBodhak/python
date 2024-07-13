# Functions

In Python, user-defined functions are a way to encapsulate reusable code blocks, improve code organization, and support modular programming.

1. Simple Function:
   A basic function that takes no parameter

   Syntax:

   ```python
   def functionName():
       statement
   ```

2. Function with parameter:
   A function that accepts an parameter

   Syntax:

   ```python
   def functionName(parameter1,parameter2):
       return Value
   ```

3. function with default Parameter:

   A function that provides a default value for parameter if no arguments are passed

   Syntax :

   ```python
   def functionName(default="value"):
       statement
   ```

4. Function with variable length arguments:

   Functions that can accept an arbitrary number of arguments using _\*args_ and _\*\*kwargs_.

   - **\*args**:

     ```python
     def sum_all(*args):
     return sum(args)

     ```

   - \***\*kwargs**:

     ```python
     def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
     ```
