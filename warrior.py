import random

class Warrior:
    def __init__(self):
        self.degat = random.randint(3, 5)
        self.chance = 5
        self.fuite = 3
        self.prix = 10
        self.type_unite = "warrior"


    def get_damage(self):
        return self.degat

    def get_chance(self):
        return self.chance

    def get_flee(self):
        return self.fuite

    def get_price(self):
        return self.prix



