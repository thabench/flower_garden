from gardenerClass import Gardener
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
               

start()
flower.set_flower_position()
gardener.set_position()
check_collision(gardener, flower)

print_map()
print(f'___YOU_ARE_AT_{gardener.y},{gardener.x}_________\n')

while game_on == True:
    
    choice = input('F - move forward,\nB - move backwards,\nR - turn right,\nL - turn left,\nX - shoot,\nQ - quit\nMake a choice:').lower()
    if choice == 'q':
        clear()
        game_on = False
        print('YOUR SCORE IS: TBA')
    elif choice == 'f':
        clear()
        if check_collision(gardener, flower) == False:
            gardener.move_forward()
        print_map()
        print(f'___YOU_MOVED_TO_{gardener.y},{gardener.x}_________\n')
    elif choice == 'b':
        clear()
        gardener.move_backwards()
        print_map()
        print(f'___YOU_MOVED_TO_{gardener.y},{gardener.x}_________\n')
    elif choice == 'r':
        clear()
        gardener.turn_right()
        print_map()
        print(f'___YOU_TURNED_RIGHT_AT_{gardener.y},{gardener.x}_________\n')
    elif choice == 'l':
        clear()
        gardener.turn_left()
        print_map()
        print(f'___YOU_TURNED_LEFT_AT_{gardener.y},{gardener.x}_________\n')
    elif choice == 'x':
        clear()
        print_map()
        print('NOT READY YET')
        # if target_hit == True:
        #     if gardener.orientation == tank_N:
        #         gardener.number_of_shots_N += 1
        #     elif gardener.orientation == tank_S:
        #         gardener.number_of_shots_S += 1
        #     elif gardener.orientation == tank_E:
        #         gardener.number_of_shots_E += 1
        #     elif gardener.orientation == tank_W:
        #         gardener.number_of_shots_W += 1
        #     else:
        #         print('Target missed')
    else:
        clear()
        print_map()
        print('WRONG CHOICE! MAKE A VALID CHOICE FROM LIST BELOW')