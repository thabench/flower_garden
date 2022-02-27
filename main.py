from gardenerClass import Gardener, Points
from flowerClass import *
from gardenVisuals import *
from highscores import GardenHighscores, session, get_highscores
from time import sleep
import os

clear = lambda: os.system('cls')
game_on = True
gardener = Gardener()
flower = Flower()
point_counter = Points()


def start():
    print('')
    print('\t\tWATER THE FLOWER\n')
    print(f'{logo}\n')
    print('\t\tLOADING...')
    sleep(3)
    clear()


def print_map():
    for line in map:
        print(f'{line}\n')


def check_collision(gardener_obj, flower_obj, position = gardener.set_position()):
    orientation = gardener_obj.get_orientation()
    
    if orientation == gardener_N and gardener_obj.y - 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_N and gardener_obj.y + 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_S and gardener_obj.y + 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_S and gardener_obj.y - 1 == flower_obj.y and gardener_obj.x == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_E and gardener_obj.y == flower_obj.y and gardener_obj.x + 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_E and gardener_obj.y == flower_obj.y and gardener_obj.x - 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_W and gardener_obj.y == flower_obj.y and gardener_obj.x - 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    elif orientation == gardener_W and gardener_obj.y == flower_obj.y and gardener_obj.x + 1 == flower_obj.x:
        print('DO NOT STEP ON FLOWERS!')
        return True
    
    elif flower_obj.x == gardener_obj.x and flower_obj.y == gardener_obj.y:
        flower_obj.set_flower_position()
        gardener_obj.x = randint(0, 9)
        gardener_obj.y = randint(0, 9)
        return True, position
    else:
        return False
    
    
def check_flower_watered(gardener_obj, flower_obj):
    orientation = gardener_obj.get_orientation()
    
    if orientation == gardener_N and gardener_obj.y > flower_obj.y and gardener_obj.x == flower_obj.x:
        print('FLOWER WATERED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_S and gardener_obj.y < flower_obj.y and gardener_obj.x == flower_obj.x:
        print('FLOWER WATERED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_E and gardener_obj.y == flower_obj.y and gardener_obj.x < flower_obj.x:
        print('FLOWER WATERED')
        flower_obj.bloom = ' '
        flower_obj.set_flower_position()
        flower_obj.x = randint(0, 9)
        flower_obj.y = randint(0, 9)
        flower_obj.bloom = 'X'
        flower_obj.set_flower_position()
        return True
    if orientation == gardener_W and gardener_obj.y == flower_obj.y and gardener_obj.x > flower_obj.x:
        print('FLOWER WATERED')
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

while True:
    first_choice = input('Enter S to START or H for HIGHSCORES: ').lower()
    if first_choice == 'h':
        clear()
        get_highscores()
    elif first_choice == 's':
        clear()
        break
    else:
        print('\n!!! Choose from H or S !!!\n')
        
flower.set_flower_position()
gardener.set_position()
check_collision(gardener, flower)
score = flower.succesfully_watered

print_map()
print(f'___YOU_ARE_AT_{gardener.y},{gardener.x}_________\n')

while game_on == True:
    
    choice = input('F - move forward,\nB - move backwards,\nR - turn right,\nL - turn left,\nX - splash water,\nI - get info\nQ - quit\nMake a choice:').lower()
    if choice == 'q':
        clear()
        if score > 0:
            player_name = input('ENTER YOUR NAME: ')
            add_highscore = GardenHighscores(player_name, score)
            session.add(add_highscore)
            session.commit()
            clear()
            get_highscores()
        else:
            point_counter.player_points = 'ZERO'
            print(f'NO FLOWERS WERE WATERED')
        game_on = False
        break
    elif choice == 'i':
        clear()
        print(gardener.get_info())
        sleep(5)
        clear()
        print_map()
    elif choice == 'f':
        clear()
        if check_collision(gardener, flower) == False:
            gardener.move_forward()
            point_counter.player_points -= 10
        print_map()
        print(f'___YOU_MOVED_TO_{gardener.y},{gardener.x}_________\n')
    elif choice == 'b':
        clear()
        if check_collision(gardener, flower) == False:
            gardener.move_backwards()
            point_counter.player_points -= 10
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
        if check_flower_watered(gardener, flower) == True:
            point_counter.player_points += 100
            score += 1
        else:
            point_counter.player_points -= 50
        print_map()
        
    else:
        clear()
        print_map()
        print('WRONG CHOICE! MAKE A VALID CHOICE FROM LIST BELOW')
    print(f'POINTS LEFT: {point_counter.player_points}')
    
    if point_counter.player_points <= 0:
        clear()
        if score > 0:
            player_name = input('ENTER YOUR NAME: ')
            add_highscore = GardenHighscores(player_name, score)
            session.add(add_highscore)
            session.commit()
            clear()
            get_highscores()
            game_on = False
        else:
            point_counter.player_points = 'ZERO'
            print(f'NO FLOWERS WERE WATERED')
        game_on = False
        