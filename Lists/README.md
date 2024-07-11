# Lists

list is a sequential collection of data, enclosed in '[]' and it is mutable means its value can be change once it is created

## Creating list

```python
my_list = [1,2,3,4,5,6]
```

## SLicing list

    Slicing allows you to access a subset of a list using the 'start:stop:step' notation:

    ```python
    my_list[1:4] # 2,3,4
    my_lis[2:] # 3,4,5,6
    my_list[::2] # 1,3,5
    ```

## list methods

- Adding Elements:

      - append(x): Adds an element x to the end of the list.
      - extend(iterable): Extends the list by appending elements from an iterable.
      - insert(i, x): Inserts element x at index i.

- Removing Elements:

      - remove(x): Removes the first occurrence of element x.
      - pop(i): Removes and returns the element at index i. If i is not specified, removes and returns the last element.
      - clear(): Removes all elements from the list.

- Finding Elements:

      - index(x): Returns the index of the first occurrence of element x.
      - count(x): Returns the number of occurrences of element x in the list.

- sorting and Reversing:

      - sort(): Sorts the list in ascending order.
      - reverse(): Reverses the elements of the list in place.

- Copying:

  - copy(): Returns a shallow copy of the list.
