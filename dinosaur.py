class Dinosaur:
    
    def __init__(self, name, health, attackpower):
        self.name = name[" "]
        self.health = health (int)
        self.attack_power = attackpower(int)
        return self.herd
    
    def attack(self, robot):
        print("A {0, name} appears...".format(robot))
        while self.health > 0 and robot.health > 0:
            self.attack(robot)
            print("Health of the {0, name} is now {0, health}." .format(robot))
            if robot.health <= 0:
                break
            robot.attack(self)
            print("Health is now {0, health}.".format(self))
        if self.health > 0:
            print("You killed the {0, name}.".format(robot))
        elif robot.health > 0:
            print("The {0, name} killed you.".format(robot))