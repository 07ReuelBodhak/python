class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    
    def display(self):
        print(f"color : {self.color}, brand : {self.brand}")

c = Car("red","toyota")
c.display()