# Advance Function

1. ## Lambda Function :

   A _lambda_ function are small anonymous function defined using lambda keyword unlike regular functions which are defined using def keyword lambda function are typically used for small operations

   Syntax :

   ```python
   lambda arguments: expression
   ```

2. ## Map

   The map function applies a given function to all items in an input list (or any iterable) and returns a map object (an iterator).

   Syntax :

   ```python
   map(function,iterable, ...)
   ```

   Example :

   ```python
   numbers = [1,3,4,5,7]
   squared = map(lambda x : x ** 2,numbers)
   print(list(squared))
   ```

3. ## Filter

   The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

   syntax :

   ```python
   filter(function, iterable)
   ```

   Example :

   ```python
    numbers = [1,2,3,4,5]
    evens = list(filter(lambda x : x % 2 == 0,numbers))
    print(evens)
   ```

4. ## Reduce

   The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

   Syntax :

   ```python
   from functools import reduce
   reduce(function, iterable[, initializer])
   ```

   Example :

   ```python
   from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    sum = reduce(lambda x, y: x + y, numbers)
    print(sum)
   ```
