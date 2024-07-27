from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def takeDamage(self):
        pass

class Health(Game):
    def __init__(self):
        self.__health = 100
    
    def getHealth(self):
        return self.__health

    def setHealth(self,health):
        if health < 0:
            print("you died")
            self.__health = 0
            return
        self.__health = health
    
    def takeDamage(self, dmg):
        Health = self.getHealth()
        Health -= dmg
        self.setHealth(Health)
        print(f"You have taken {dmg} damage")
        print(f"your current heath : {self.getHealth()}")

class Bomb(Health):
    def Burn(self):
        self.takeDamage(10)
    
h = Health()
b = Bomb()
b.Burn()
b.Burn()