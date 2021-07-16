from weapon import Weapon


class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon
        
    
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health = self.attack_power
        print("Attack succesful! Robot health now is {dinosaur.health}")
        