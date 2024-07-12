# Dictionary in python

Dictionaries are used to store data values in key:value pairs

## Dictionaries Methods

1. **clear()**: Removes all items from dictionaries

2. **copy()** : Returns a shallow copy of the dictionary

3. **fromkeys(seq, value=None)** : the purpose of this method is to create a new dictionary from a 'seq' like list and set its values to 'value'

4. **get(key,value=None)** : Returns the value for key is key not exists it return the default value its usefull for accessing dictionary element while avoiding error

5. **items()** : Returns a view object that displays a list of a dictionary's key-value tuple pairs.

6. **keys()** : Returns a view object that displays a list of all the keys in the dictionary.

7. **pop(key,default=None)** : Removes a specified key and returns the corresponding value. if the key is not found default is return

8. **popitem()** : Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.

9. **setdefault(key, default=None)** : Returns the value of key if key is in the dictionary. If not, it inserts key with a value of default and returns default.

10. **update([other])** : Updates the dictionary with the key-value pairs from other, overwriting existing keys.
