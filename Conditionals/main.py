## if else
a = 10
b = 30
c = 40

if a > b :
    print(f"{a} is greater than {b}")
else :
    print(f"{b} is greater than {a}")

## if elif else

if a > b and a > c:
    print(f"{a} is greater than {b} and {c}")
elif b > a and b > c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")

## short hand if else

print(f"{a} is greater") if a > b else print(f"{b} is greater")
