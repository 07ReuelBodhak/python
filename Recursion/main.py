def reverse(n):
    if n == 0:
        return
    print(n)
    return reverse(n - 1)

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def prime(n,divisor = None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = int(n ** 0.5)
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return prime(n,divisor - 1)
    
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci (n - 2)

def sum(l,i=0,total=0):
    if i == len(l):
        return total
    total += l[i]
    return sum(l,i + 1,total)

def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

print(sum_num(5))

# reverse(5)
#print(factorial(5))
# print(prime(7))
# print(fibonacci(12))
# print(sum([1,2,3,4]))

'''
n = 5

5 + sum_num(4)
return 5 + 10 = 15

4 + sum_num(3)
return 4 + 6 = 10

3 + sum_num(2)
return 3 + 3 = 6

2 + sum_num(1)
return 2 + 1 = 3

1 + sum_num(0)
return 1 + 0 = 1

'''