# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

def clear_console():
    from sys import platform
    import os
    if 'win' in platform:
        os.system('CLS')
    elif 'lin' in platform:
        os.system('clear')


def show_status(candy_amount):
    print(f'Сейчас на столе {candy_amount} конфет')


def gamer_move(gamer_name):
    gamer_candy = int(input('Игрок {gamer_name}, Сколько конфет возьмёте? '))
    return gamer_candy


clear_console()
start_candy = int(input('Введите исходное количество конфет: '))
clear_console()
current_candy = start_candy
show_status(current_candy)
current_gamer = 1


while current_candy > 0:
    candy_dec = gamer_move(current_gamer)
    clear_console()
    current_candy -= candy_dec
    show_status(current_candy)

    if current_candy == 0:
        print(f'Игрок {current_gamer} выиграл')
    elif current_gamer == 1:
        current_gamer = 2
    elif current_gamer == 2:
        current_gamer = 1
