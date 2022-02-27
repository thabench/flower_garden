from gardenerClass import Gardener, Points
from flowerClass import *
from gardenVisuals import *
from time import sleep
import os

clear = lambda: os.system('cls')
game_on = True


def start():
    print('')
    print('\t\tWATER THE FLOWER\n')
    print(f'{logo}\n')
    print('\t\tLOADING...')
    sleep(3)
    clear()

gardener = Gardener()
flower = Flower()
point_counter = Points()

def print_map():
    for line in map:
        print(f'{line}\n')

def check_collision(gardener_obj, flower_obj, position = gardener.set_position()):
    orientation = gardener_obj.get_orientation()
    
    if orientation == gardener_N and gardener_obj.y - 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    if orientation == gardener_S and gardener_obj.y + 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    if orientation == gardener_E and gardener_obj.y == flower_obj.y and gardener_obj.x + 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    if orientation == gardener_W and gardener_obj.y == flower_obj.y and gardener_obj.x - 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    
    elif flower_obj.x == gardener_obj.x and flower_obj.y == gardener_obj.y:
        flower_obj.set_flower_position()
        gardener_obj.x = randint(0, 9)
        gardener_obj.y = randint(0, 9)
        return True, position
    else:
        return False
    
def check_flower_waterred(gardener_obj, flower_obj):
    orientation = gardener_obj.get_orientation()
    
    if orientation == gardener_N and gardener_obj.y > flower_obj.y and gardener_obj.x == flower_obj.x:
        print('FLOWER WATERRED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_S and gardener_obj.y < flower_obj.y and gardener_obj.x == flower_obj.x:
        print('FLOWER WATERRED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_E and gardener_obj.y == flower_obj.y and gardener_obj.x < flower_obj.x:
        print('FLOWER WATERRED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_W and gardener_obj.y == flower_obj.y and gardener_obj.x > flower_obj.x:
        print('FLOWER WATERRED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    else:
        print('FLOWER MISSED')
        return False
         

start()
flower.set_flower_position()
gardener.set_position()
check_collision(gardener, flower)

print_map()
print(f'___YOU_ARE_AT_{gardener.y},{gardener.x}_________\n')

while game_on == True:
    
    choice = input('F - move forward,\nB - move backwards,\nR - turn right,\nL - turn left,\nX - splash water,\nI - get info\nQ - quit\nMake a choice:').lower()
    if choice == 'q':
        clear()
        game_on = False
    elif point_counter.player_points == 0:
        print ('OUT OF POINTS! YOUR SCORE IS: ')
    elif choice == 'i':
        print(gardener.get_info())
    elif choice == 'f':
        clear()
        if check_collision(gardener, flower) == False:
            gardener.move_forward()
            point_counter.player_points -= 10
        print_map()
        print(f'___YOU_MOVED_TO_{gardener.y},{gardener.x}_________\n')
    elif choice == 'b':
        clear()
        gardener.move_backwards()
        point_counter.player_points -= 10
        print_map()
        print(f'___YOU_MOVED_TO_{gardener.y},{gardener.x}_________\n')
    elif choice == 'r':
        clear()
        gardener.turn_right()
        point_counter.player_points -= 10
        print_map()
        print(f'___YOU_TURNED_RIGHT_AT_{gardener.y},{gardener.x}_________\n')
    elif choice == 'l':
        clear()
        gardener.turn_left()
        point_counter.player_points -= 10
        print_map()
        print(f'___YOU_TURNED_LEFT_AT_{gardener.y},{gardener.x}_________\n')
    elif choice == 'x':
        clear()
        gardener.make_a_splash()
        if check_flower_waterred(gardener, flower) == True:
            point_counter.player_points += 100
        else:
            point_counter.player_points -= 10
        print_map()
        
    else:
        clear()
        print_map()
        print('WRONG CHOICE! MAKE A VALID CHOICE FROM LIST BELOW')
    print(f'POINTS: {point_counter.player_points}')