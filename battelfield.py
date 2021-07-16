from fleet import Fleet
from herd import Herd




class Battelfield:
    
    def __init__(self, fleet, herd):
        self.fleet = Fleet()
        self.herd = Herd()
        
    
    def run_game(self):
        self.display_welcome()
        self.battle()
        self.diplay_winners()
    
    def display_welcome(self):
        print("Welcom to Robots vs. Dinosaurs")
    
    def battle(self):
        while len(self.herd.dinosaur) > 0 and len(self.fleet.robot) > 0:
            self.robo_turn()
            self.dino_turn()
    
    def dino_turn(self):
        self.show_dino_opponent_options()
        dinosaur_choice = int(input("Which dinosaur will attack"))
        self.show_robo_opponent_options()
        dino_choice = int(input("Which robot will defend"))
        self.fleet.robot[dino_choice].attack(
            self.fleet.robot[robo_choice])
        if self.fleet.robo[robo_choice].health <= 0:
            self.fleet.robo.remove(self.robo[robo_choice])
    
    def robo_turn(self):
        self.show_robo_opponent_options()
        robot_choice = int(input("Which robot will attack"))
        self.show_dino_opponent_options()
        dino_choice = int(input("Which dinosaur will defend"))
        self.fleet.robot[robot_choice].attack(
            self.herd.dinosaur[dino_choice])
        if self.herd.dinosaur[dino_choice].health <= 0:
            self.herd.dinosaur.remove(self.dinosaur[dino_choice])
        
    
    def show_dino_opponent_options(self):
        print("Choose dinosaur")
        index = 0
        for dinosaur in self.herd.dinosaur:
            print("print {index} for {dinosaur.name} with {dinosaur.health!}")
    
    def show_robo_opponent_options(self):
        print("Choose robot")
        index = 0
        for robot in self.fleet.robots:
            print("print {index} for {robot.name} with {robot.health!}")
    
    def diplay_winners(self):
        if len(self.fleet.robot) > len(self.herd.dinosaur):
            print("robot wins!")
        else:
            print("dinosaur wins!")
            
        