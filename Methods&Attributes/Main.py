class Plane:
    #class Attributes
    wheels = 3
    wings = 2

    def __init__(self,color,capacity):
        self.color = color
        self.capacity = capacity
    
    ## Instance Method
    def printDetails(self):
        print(f"Plane Color : {self.color}, Plane Capacity : {self.capacity}")
        print(f"Plane Wheels : {self.wheels}, plane Wings : {self.wings}")

    ##class Methods
    @classmethod
    def modifyStructure(cls,wheel,wing):
        cls.wheels = wheel
        cls.wings = wing
    
    ##Static Method
    @staticmethod
    def isPlane():
        return True

p = Plane("white",344)
p.printDetails()

Plane.modifyStructure(4,3)
p.printDetails()

print(p.isPlane())
print(Plane.isPlane())