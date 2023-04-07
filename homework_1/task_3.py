"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо
исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

import random


def generate_random_numbers(a, b):
    rand_list = []
    rand_dict = {}
    for elem in range(10):
        number = random.randint(a, b)
        while number == 0:
            number = random.randint(a, b)
        rand_list.append(number)
        rand_dict.update({f'elem_{elem}': number})
    return rand_list, rand_dict


print(generate_random_numbers(-3, 25))
