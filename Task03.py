# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def input_string():
    local_string = input('Введите текст: ')
    return local_string

def decompress(string_to_decompress):
    decompressed_string = ''
    for i in range(len(string_to_decompress)):
        if string_to_decompress[i].isdigit():
            decompressed_string += string_to_decompress[i+1]*int(string_to_decompress[i])
    return decompressed_string

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
    target_string = decompress(initial_string)
    print('Востановленная строка:')
    print(target_string)

else:
    target_string = compress(initial_string)
    print('Сжатая строка:')
    print(target_string)