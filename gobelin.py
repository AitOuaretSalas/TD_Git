import random

class Gobelin:
    def __init__(self):
        self.degat = random.randint(2, 3)
        self.loot = random.uniform(1, 1.5)
        
    def get_damage(self):
        return self.degat
    
    def get_loot(self):
        return self.loot
    
    def get_unit_type(self):
        return "Gobelin"
    
    
    
    
