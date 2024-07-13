## lambda function
from functools import reduce

add = lambda x,y : x + y
print(add(2,3))

## map function
def factorial(x):
    fact = 1
    if x == 0:
        return 1
    else:
        for i in range(1,x + 1):
            fact = fact * i
    return fact

l = [1,2,3,4,5,6]
newl = list(map(factorial,l))
print("factorials : ",newl)

newl2 = list(map(lambda x : x * x * x,l))
print("cubes : ",newl2)

## filter function

ages = [15,43,23,18,19,34,11]
allowed = list(filter(lambda x : x > 18,ages))
print(allowed)

odds = list(filter(lambda x : x % 2 != 0,ages))
print(odds)

## Reduce function

numbers = [1,2,3,7,9,4,6]

# now we have to find the biggest number from the list

big = reduce(lambda x,y: x if x > y else y,numbers)
print(big)

'''
now lets understand how this all works 
in first iteration the reduce function takes 2 arguments in our case 1 and 2 
now based on our condition 2 is greater so it will return 2 
now our numbers will be [2,3,7,9,4,6]
again out function applies 
and numbers will be [3,7,9,4,6]

hence this continues until we find a biggest number
'''