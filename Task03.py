# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def input_string():
    local_string = input('Введите текст: ')
    return local_string

def decompress(string_to_decompress):
    pass

def compress(string_to_compress):
    compressed_string = ''
    current_sign = string_to_compress[0]
    signs_counter = 1
    compressed_part = current_sign
    for i in range(1,len(string_to_compress)):
        if string_to_compress[i] == current_sign:
            signs_counter += 1
            compressed_part = str(signs_counter) + current_sign
        else:
            compressed_string += compressed_part
            compressed_part = string_to_compress[i]
            current_sign = string_to_compress[i]
            signs_counter = 1
    compressed_string += compressed_part
    return compressed_string

initial_string = input_string()


if initial_string[0].isdigit():
    decompress(initial_string)
else:
    target_string = compress(initial_string)
    print(target_string)