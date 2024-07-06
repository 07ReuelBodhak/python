## numeric types

a = 12 #int
b  = 12.4 #float
c = 3 + 4j #complex

print(f"type of a {type(a)}, type of b {type(b)}, type of c {type(c)}")

## perform basic arithmetic operations on complex datatypes

complex_num1  = 2 + 2j
complex_num2 = 1 - 3j

z1 = complex_num1 + complex_num2
z2 = complex_num1 - complex_num2
z3 = complex_num1 / complex_num2
z4 = complex_num1 * complex_num2

print(f"result of addition {z1}\nresult of substraction {z2}\nresult of division {z3}\nresult of multiplication {z4}\n")

## Sequence types

str = "Hello" # string
list = [1,2,3] # list
tuple = (1,2,3) # tuple
rng = range(3) # range

print(f"String : {str}\nList : {list}\nTuple : {tuple}\nRange : {rng}")

## Mapping type

dict = {"name" : "roy","age" : "20"}
print(f"Dictionary : {dict}")

## set Types

set1 = {1,2,3,5}
set2 = frozenset([1,2,3,4])

print(f"set : {set1}\nFrozen set:  {set2}")

## Boolean Types 

boolean = True
print(f"boolean value : {boolean}")

## Binary Types

byte = b'hello'
byteArray = bytearray(b'Hello')
memoryView = memoryview(b'hello')

print(f"bytes : {byte}\nbytes array : {byteArray}\nmemory view : {memoryView}")

## None Types

value = None
print(f"None vale : {value}")