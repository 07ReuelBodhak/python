# Recursion

Recursion in Python is a method where a function calls itself to solve a smaller instance of the same problem. It's useful for problems that can be broken down into similar sub-problems.

```python
def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output will be 120
```

In this example:

- The `factorial` function calls itself with a decremented value of `n`.
- The base case (`if n == 1`) stops the recursion.
- The recursive case (`n * factorial(n - 1)`) continues the process until it reaches the base case.
