# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def input_string():
    local_string = input('Введите текст: ')

initial_string = input_string()

if initial_string[0].isdigit():
    print('yes')