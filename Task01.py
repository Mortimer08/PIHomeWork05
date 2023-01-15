# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

from sys import platform
import os
from random import randint


def clear_console():

    if 'win' in platform:
        os.system('CLS')
    elif 'lin' in platform:
        os.system('clear')


def show_status(candy_amount, candy_max):
    print(f'Сейчас на столе {candy_amount} конфет')
    print(f'За один ход можно брать не больше {candy_max} конфет')


def gamer_move(gamer_name):
    gamer_candy = int(input(f'Игрок {gamer_name}, Сколько конфет возьмёте? '))
    return gamer_candy


def bot_move(candy_on_table, candy_max):
    if candy_on_table <= candy_max:
        bot_takes = candy_on_table
    elif candy_on_table % candy_max > 1:
        bot_takes = candy_on_table % candy_max-1
    else:
        bot_takes = 1
    return bot_takes


clear_console()

start_candy = int(input('Введите исходное количество конфет: '))

clear_console()
current_candy = start_candy
limit_to_take = 28
if randint(1, 2) == 1:
    current_gamer = 'Бот'
else:
    current_gamer = 'Человек'

print(f'Первым ходит игрок {current_gamer}')


while current_candy > 0:
    current_limit = limit_to_take if limit_to_take < current_candy else current_candy
    show_status(current_candy, current_limit)
    bot_move(current_candy, limit_to_take)
    if current_gamer == 'Бот':
        candy_dec = bot_move(current_candy, limit_to_take)
        print(f'Бот забрал {candy_dec} конфет')
        input()
    else:
        candy_dec = gamer_move(current_gamer)
    if candy_dec > current_candy or candy_dec > limit_to_take:
        clear_console()
        print('Перебор! Берите меньше')
    else:
        clear_console()
        current_candy -= candy_dec
        if current_candy == 0:
            print(f'Игрок {current_gamer} выиграл!')
        elif current_gamer == 'Бот':
            current_gamer = 'Человек'
        elif current_gamer == 'Человек':
            current_gamer = 'Бот'
