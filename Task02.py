# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from sys import platform
import os
from random import randint


def clear_console():

    if 'win' in platform:
        os.system('CLS')
    elif 'lin' in platform:
        os.system('clear')

clear_console()

