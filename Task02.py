# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from sys import platform
import os
from random import randint

gamer_1_name = '1'
gamer_2_name = '2'

sing_1_name = 'X'
sing_2_name = 'O'


def clear_console():

    if 'win' in platform:
        os.system('CLS')
    elif 'lin' in platform:
        os.system('clear')


def show_field(local_field):
    count = 0
    for place_key in local_field:
        print(local_field[place_key], end=' ')
        count += 1
        if count == 3:
            print()
            count = 0
    print()


def gamer_move(local_gamer, local_sign):
    while True:
        gamer_place = input(
            f'Игрок {local_gamer} куда поставите {local_sign}? ')
        if gamer_place.isdigit():
            return int(gamer_place)
    # else:
    #     gamer_place = int(
    #     input(f'Игрок {local_gamer} куда поставите {local_sign}? '))


def field_is_full(local_field):
    for place_key in local_field:
        if local_field[place_key].isdigit():
            return False
    return True


def move_is_possible(local_move):
    if str(move).isdigit() and move > 0 and move < 10 and str(move) in field.values():
        return True
    else:
        return False


def sing_wins(local_field, local_sign):
    local_vertical_1 = local_field[1] == local_sign and local_field[4] == local_sign and local_field[7] == local_sign
    local_vertical_2 = local_field[2] == local_sign and local_field[5] == local_sign and local_field[8] == local_sign
    local_vertical_3 = local_field[3] == local_sign and local_field[6] == local_sign and local_field[9] == local_sign
    local_gorizontal_1 = local_field[1] == local_sign and local_field[2] == local_sign and local_field[3] == local_sign
    local_gorizontal_2 = local_field[4] == local_sign and local_field[5] == local_sign and local_field[6] == local_sign
    local_gorizontal_3 = local_field[7] == local_sign and local_field[8] == local_sign and local_field[9] == local_sign
    local_diagonal_1 = local_field[1] == local_sign and local_field[5] == local_sign and local_field[9] == local_sign
    local_diagonal_2 = local_field[3] == local_sign and local_field[5] == local_sign and local_field[7] == local_sign
    if local_vertical_1 or local_vertical_2 or local_vertical_3 \
        or local_gorizontal_1 or local_gorizontal_2 or local_gorizontal_3 \
            or local_diagonal_1 or local_diagonal_2:
        return True
    else:
        return False


def change_sign(local_sign):
    if local_sign == sing_1_name:
        local_sign = sing_2_name
    else:
        local_sign = sing_1_name
    return local_sign


def change_gamer(local_gamer):
    if local_gamer == gamer_1_name:
        local_gamer = gamer_2_name
    else:
        local_gamer = gamer_1_name
    return local_gamer


# def move_possible(place):
#     for row in field:
#         if place in row:
#             return True
#     return False


# def make_move(local_field, place):
#     for row in local_field:
#         if place in row:
#             rep
#     return False


field = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9',
}
current_sign = sing_1_name
if randint(1, 2) == 1:
    current_gamer = gamer_1_name
else:
    current_gamer = gamer_2_name

clear_console()

while not field_is_full(field):

    show_field(field)
    
    move = gamer_move(current_gamer, current_sign)
    clear_console()
    if move_is_possible(move):
        field[move] = current_sign
        if sing_wins(field, current_sign):
            show_field(field)
            print(f'Игрок {current_gamer} ({current_sign}) выиграл!')
            break
        current_sign = change_sign(current_sign)
        current_gamer = change_gamer(current_gamer)
    else:
        print('Такой ход недопустим!')
        print()


print('Игра закончена!')
