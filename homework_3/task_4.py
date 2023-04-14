"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если
файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам
функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться
ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод
содержимого. Вся программа должна запускаться по вызову первой функции.
"""

import os
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def print_file(file):
    with open(file, 'r', encoding='utf-8') as r:
        for line in r:
            print(line)


def create_file(name, lines):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует!')
        return False
    with open(name, 'a', encoding='utf-8') as f:
        strings = [generate_random_string(10) for _ in range(10)]
        numbers = [random.randint(1, 100) for _ in range(lines)]
        strings_numbers = zip(strings, numbers)
        for el in strings_numbers:
            f.write(f'{el[0]} {el[1]}\n')
    print_file(os.path.join(os.getcwd(), name))


create_file('task_4_testfile.txt', 10)
