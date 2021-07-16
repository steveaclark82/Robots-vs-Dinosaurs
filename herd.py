from dinosaur import Dinosaur


class Herd:
    
    def __init__(self):
        self.dinosaur = []
        
    def create_herd(self):
        
        dinosaur1 = Dinosaur('Trex')
        dinosaur2 = Dinosaur('Raptor')
        dinosaur3 = Dinosaur('Trycera') 
        
        self.dinosaur.append(dinosaur1)
        self.dinosaur.append(dinosaur2)
        self.dinosaur.append(dinosaur3)
    