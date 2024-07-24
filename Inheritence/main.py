class Vehicle:
    def __init__(self,wheels,weight):
        self.wheels = wheels
        self.weight = weight

class Bike(Vehicle):
    def __init__(self, wheels, weight,color,brand):
        super().__init__(wheels, weight)
        self.color = color
        self.brand = brand
    
    def details(self):
        print("Color : ",self.color)
        print("brand : ",self.brand)
        print("wheels : ",self.wheels)
        print("weight : ",self.weight,"kg")
    
    def isBike(self):
        if self.wheels == 2:
            return True

class Car(Vehicle):
    def __init__(self, wheels, weight,color,brand):
        super().__init__(wheels, weight)
        self.color = color
        self.brand = brand
    
    def details(self):
        print("Color : ",self.color)
        print("brand : ",self.brand)
        print("wheels : ",self.wheels)
        print("weight : ",self.weight,"kg")
    
    def isCar(self):
        if self.wheels == 4:
            return True

c = Car(4,1000,"blue","toyota")
b = Bike(2,180,"red","Ninja")
c.details()
b.details()
print("is car : ",c.isCar())
print("is bike : ",b.isBike())