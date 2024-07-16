# Exception handling

Exception handling in Python is a mechanism to handle errors gracefully without terminating the program abruptly. It allows the programmer to deal with unexpected situations by catching exceptions and providing alternative solutions or corrective actions.

## Basic Exception Handling

### Try and Except Block

The try block lets you test a block of code for errors, while the except block lets you handle the error

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
```

### Multiple Except Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Value !")
```

### Catching multiple Exception

you can catch multiple exceptions in a single except block by specifying a tuple of exceptions.

```python
try:
    result = 10 / 0
except(ZeroDivisionError,ValueError):
    print("An error occurred")
```

### Else Block

the else block executes when no exception are raised

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result: ",result)
```

### Finally Block

The finally block will execute no matter what, whether an exception occurs or not. This is useful for cleaning up resources, such as closing files or network connections.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result: ",result)
finally:
    print("this block will always executes")
```

### Raising an Exception

you can raise exception using the 'raise' statement.
this is useful for triggering exceptions manually.

```python
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

try :
    result = divide(10,0)
except ZeroDivisionError as e:
    print(e)
```

### Custom Exceptions

You can define your own exceptions by creating a new class that inherits from the built-in Exception class.

```python
class CustomError(Exception):
pass

def risky_function():
raise CustomError("Something went wrong!")

try:
risky_function()
except CustomError as e:
print(e)
```

### Best Practices

1.  Be specific with exceptions: Catch specific exceptions rather than using a broad except clause.

```python
try: # risky code
except KeyError: # handle KeyError specifically
```

2.  Avoid bare except: Avoid using except: without specifying an exception type. This can catch unexpected exceptions and make debugging difficult.

    ```python
    try: # risky code
    except Exception as e: # handle all exceptions
    print(e)
    ```

3.  Clean up with finally: Use finally to ensure that resources are released, such as closing files or network connections.

    ```python
    try:
    file = open('file.txt', 'r') # process file
    except IOError as e:
    print(e)
    finally:
    file.close()
    ```

4.  Log exceptions: Log exceptions to keep track of errors that occur during the execution of your program.

    ```python
    import logging

    logging.basicConfig(level=logging.ERROR)

    try: # risky code
    except Exception as e:
    logging.error(e)
    ```

By using these exception handling techniques, you can write more robust and error-tolerant Python code.
