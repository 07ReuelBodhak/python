# Decorators

Decorators are a powerful and expressive tool in python that allows you to modify the behavior of a function or a class. They are often used to add "wrapping" functionality to existing code in a clean, readable, and reusable way. Decorators are applied using the '@' symbol above a function or a method.

### Basic Syntax

A decorator is essentially a callable (usually a function) that takes a function as an argument and returns a new function that typically extends the behavior of the original function

```python
def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("hello !")

say_hello()
```

In this example:

- my_decorator is the decorator function.

- say_hello is the function being decorated.

- When say_hello is called, it first executes the code in wrapper, then calls say_hello, and finally executes the code after the original function call.

### Common use cases

1. **Logging**:

   A logging decorator is used to log the function calls and their results. It's helpful for debugging and monitoring purposes.

   ```python
    def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

    @log_decorator
    def say_hello(name):
        return f"Hello {name}"

    say_hello("alex")
   ```

2. **Access Control** :
   An access control decorator ensures that a function can only be executed if certain conditions (like authentication) are met.

   ```python
   authenticated = False

   def requires_authentication(func):
       def wrapper(*args, **kwargs):
           if not authenticated:
               raise Exception("Authentication Error")
           return func(*args, **kwargs)
       return wrapper

   def login(password):
       if password == 123:
           return True
       return False

   password = int(input("please enter pass : "))
   authenticated = login(password)

   @requires_authentication
   def getData():
       return "sensitive data"

   try:
       data = getData()
       print(data)
   except Exception as e:
       print("Error : ",e)

   ```

3. Caching Decorator

   ```python
   def cache_decorator(func):
   cache = {}
   def wrapper(*args):
       if args in cache:
           return cache[args]
       result = func(*args)
       cache[args] = result
       return result
   return wrapper

   @cache_decorator
   def slow_function(n):
       from time import sleep
       sleep(4)
       return n * n

   print(slow_function(2))
   print(slow_function(2))
   ```
