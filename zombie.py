import random

class Zombie:
    def __init__(self):
        self.degat = random.uniform(1, 2)
        self.loot = random.uniform(0.5, 1)
        
    def get_damage(self):
        return self.degat
    
    def get_loot(self):
        return self.loot
    
    
    def get_unit_type(self):
        return "Zombie"
    
    
