class Dinosaur:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 50

    
    def attack(self, robot):
        robot.health = robot.health = self.attack_power
        print("Attack succesful! Robot health now is {robot.health}")
        