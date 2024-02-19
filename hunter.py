import random

class Hunter:
    def __init__(self):
        self.degat = random.randint(1, 2)
        self.chance = 10
        self.fuite = 20
        self.prix = 25
        self.type_unite = "hunter"


    def get_damage(self):
        return self.degat
    
    def get_chance(self):   
        return self.chance
    

    def get_flee(self):
        return self.fuite
    
    def get_price(self):
        return self.prix
    
