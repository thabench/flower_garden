from gardenVisuals import *
from flowerClass import Flower
from random import randint, choice

random_num_x = randint(0, 9)
random_num_y = randint(0, 9)

class Gardener():
    def __init__(self, x=random_num_x, y=random_num_y):
        self.x = x
        self.y = y
        self.orientation = choice(gardener_positions)
        self.number_of_splashes_N = 0
        self.number_of_splashes_S = 0
        self.number_of_splashes_E = 0
        self.number_of_splashes_W = 0
        if(x < 0 or y < 0):
            raise ValueError("Only positive coordinates!")

    def get_position(self):
        return self.x, self.y
    
    def set_position(self):
        position =  map[self.y][self.x] = self.orientation
        return position

    def get_orientation(self):
        return self.orientation
    
    def move_forward(self):
        if self.orientation == gardener_N:
            self.orientation = gardener_B
            self.set_position()
            if self.y == 0:
                self.orientation = gardener_N
                return self.set_position()
            self.y -= 1
            self.orientation = gardener_N
            return self.set_position()
        elif self.orientation == gardener_S:
            self.orientation = gardener_B
            self.set_position()
            if self.y == 9:
                self.orientation = gardener_S
                return self.set_position()
            self.y += 1
            self.orientation = gardener_S
            return self.set_position()
        elif self.orientation == gardener_W:
            self.orientation = gardener_B
            self.set_position()
            if self.x == 0:
                self.orientation = gardener_W
                return self.set_position()
            self.x -= 1
            self.orientation = gardener_W
            return self.set_position()
        elif self.orientation == gardener_E:
            self.orientation = gardener_B
            self.set_position()
            if self.x == 9:
                self.orientation = gardener_E
                return self.set_position()
            self.x += 1
            self.orientation = gardener_E
            return self.set_position()
    
    def move_backwards(self):
        if self.orientation == gardener_N:
            self.orientation = gardener_B
            self.set_position()
            if self.y == 9:
                self.orientation = gardener_N
                return self.set_position()
            self.y += 1
            self.orientation = gardener_N
            return self.set_position()
        elif self.orientation == gardener_S:
            self.orientation = gardener_B
            self.set_position()
            if self.y == 0:
                self.orientation = gardener_S
                return self.set_position()
            self.y -= 1
            self.orientation = gardener_S
            return self.set_position()
        elif self.orientation == gardener_W:
            self.orientation = gardener_B
            self.set_position()
            if self.x == 9:
                self.orientation = gardener_W
                return self.set_position()
            self.x += 1
            self.orientation = gardener_W
            return self.set_position()
        elif self.orientation == gardener_E:
            self.orientation = gardener_B
            self.set_position()
            if self.x == 0:
                self.orientation = gardener_W
                return self.set_position()
            self.x -= 1
            self.orientation = gardener_E
            return self.set_position()
    
    def turn_left(self):
        if self.orientation == gardener_N:
            self.orientation = gardener_W
            return self.set_position()
        elif self.orientation == gardener_W:
            self.orientation = gardener_S
            return self.set_position()
        elif self.orientation == gardener_S:
            self.orientation = gardener_E
            return self.set_position()
        elif self.orientation == gardener_E:
            self.orientation = gardener_N
            return self.set_position()
    
    def turn_right(self):
        if self.orientation == gardener_N:
            self.orientation = gardener_E
            return self.set_position()
        elif self.orientation == gardener_E:
            self.orientation = gardener_S
            return self.set_position()
        elif self.orientation == gardener_S:
            self.orientation = gardener_W
            return self.set_position()
        elif self.orientation == gardener_W:
            self.orientation = gardener_N
            return self.set_position()

    def make_a_splash(self):
        if self.orientation == gardener_N:
            self.number_of_splashes_N += 1
        elif self.orientation == gardener_S:
            self.number_of_splashes_S += 1
        elif self.orientation == gardener_E:
            self.number_of_splashes_E += 1
        elif self.orientation == gardener_W:
            self.number_of_splashes_W += 1
            
    
    def get_info(self):
        return f'''\tGardener is facing {self.get_orientation()}\n
        Gardener is at {self.x, self.y}\n
        Total Splashes made: {sum([self.number_of_splashes_N, self.number_of_splashes_S, self.number_of_splashes_E, self.number_of_splashes_W])}\n
        Splashed north: {self.number_of_splashes_N}\n
        Splashed south: {self.number_of_splashes_S}\n
        Splashed east: {self.number_of_splashes_E}\n
        Splashed west: {self.number_of_splashes_W}\n'''
                    
class Points():
    def __init__(self):
        self.player_points = 100
        