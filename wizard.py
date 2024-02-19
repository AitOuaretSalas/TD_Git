import random

class Wizard:
    def __init__(self):
        self.degat = random.randint(2, 4)
        self.chance = 20
        self.fuite = 10
        self.prix = 15
        self.type_unite = "wizard"


    def get_damage(self):
        return self.degat
    
    def get_chance(self):
        return self.chance
    
    def get_flee(self):
        return self.fuite
    
    def get_price(self):
        return self.prix
    
    