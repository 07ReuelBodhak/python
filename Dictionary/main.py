## dictionary 

my_dict = {"name" : "roy", "age" : "20", "gender" : "male"}

keys = ["height","width","area"]
values = 0

new_dict = dict.fromkeys(keys,values)
print("new_dict : ",new_dict)

print(my_dict.get("age",0))

my_dict.setdefault("hobby","drawing")
print(my_dict)

my_dict.update({"experience" : "6 months"})
print(my_dict)