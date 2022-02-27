from gardenVisuals import *
from random import randint, choice

random_num_x = randint(0, 9)
random_num_y = randint(0, 9)

class Flower():
    def __init__(self, x=random_num_x, y=random_num_y):
        self.x = x
        self.y = y
        self.bloom = flower_on_map
        self.succesfully_watered = 0
        if(x < 0 or y < 0):
            raise ValueError("Only positive coordinates!")
        
    def set_flower_position(self):
        position =  map[self.y][self.x] = self.bloom
        return position
    
    def get_flower_position(self):
        return self.x, self.y
        
        