## open file in reading mode

file = open("example.txt","r")
content = file.read()
print(content)

file.seek(0)
line = file.readline()

file.seek(0)
lines = file.readlines()

print("single line : ",line)
print("multiple lines : ",lines)

file.close()

## writing mode

file = open("abc.txt","w")
file.write("frogs croak\n")
file.writelines(["Rains Soak\n","Chicks peep\n","Crickets leap\n",
                "Bees hum\n","Robins come\n","Birds sing\n",
                "It's Spring!\n"])
file.close()

file = open("abc.txt","r")
content = file.read()
print(content)
file.close()

## reading and writing file with "with" statement

with open("example.txt","a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    file.write("\nwritten by St.Jerome")
    file.seek(0)
    content = file.read()
    print("after adding author : ",content)
    file.close()