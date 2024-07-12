# Sets

sets are used to store multiple items in a single variable

A set is a collection which is unordered, unchangeable\*, and unindexed.

- **set constructor** : The set() constructor can be used to create a set. If you pass an iterable (like a list), it will convert it into a set with unique elements. To create an empty set, you must use set() because {} creates an empty dictionary.

## Set methods

- **add()** : Adds an element in the set if the element already exists the set remain unchanged

- **clear()** : Removes all elements from the set

- **copy()** : Returns a shallow copy of a set

- **difference(\*others)** : returns a new set containing unique elements from both set

- **difference_update(\*others)** : Removes element from a set that are also present in other set

- **discard(elem)** : removes element from a set if its a member if its not a member do nothing

- **intersection(others)** : returns a new set containing element that are common in bot sets

- **intersection_update(other)** : keep element that are common in both set else remove unique one

- **isdisjoint(others)** : returns true if there is no unique common element in both sets

- **issubset(other)** : return true if one set is subset of others means if one set have all element present in other set

- **issuperset(other)** : returns true if the set is a superset of others

- **symmetric_difference(other)** : returns a new set containing element that are present in both sets but does not include the common elements

- **symmetric_difference_update(other)** : Updates the set, keeping only elements found in either the set or other but not in both.

- **union** : Returns a new set with elements from the set and all others
