class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property 
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not value:
            raise ValueError("Age cannot be empty")
        self._age = value
    
    @age.deleter
    def age(self):
        print("Deleting age")
        del self._age
    

p = Person("alex", 34)
print(p.name)  
print(p.age)   

p.name = "ace"
p.age = 43
print(p.name)  
print(p.age)

del p.age  
