import random

class Orc:
    def __init__(self):
        self.degat = random.uniform(3, 5)
        self.loot = random.uniform(2, 2.5)
    
    def get_damage(self):
        return self.degat
    
    def get_loot(self):
        return self.loot
    
    
    def get_unit_type(self):
        return "Orc"

