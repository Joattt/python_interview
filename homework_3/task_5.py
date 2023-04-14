"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

import os
import random
import string
import re


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def print_file_and_replace(file, substring):
    with open(file, 'r', encoding='utf-8') as r:
        text = r.read()
        pattern = f'{substring}\d*'
        new_value = 'example345'
        print(re.search(pattern, text))
        print(re.findall(pattern, text))
        text = re.sub(pattern, new_value, text)
    with open(file, 'w+', encoding='utf-8') as x:
        x.write(text)
    lets_nums_spaces = '\s+\d+[a-zA-Z]+\w*\s+|\s+[a-zA-Z]+\d+\w*\s+'

    for el in re.findall(lets_nums_spaces, text):
        print(el)


def create_file(name, lines):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует!')
        return False
    with open(name, 'a', encoding='utf-8') as f:
        strings = [generate_random_string(10) for _ in range(10)]
        numbers = [random.randint(1, 100) for _ in range(lines)]
        for idx in range(0, len(numbers), 3):
            numbers[idx] = f'example{numbers[idx]}'
        strings_numbers = zip(strings, numbers)
        for el in strings_numbers:
            f.write(f'{el[0]} {el[1]}\n')
    print_file_and_replace(os.path.join(os.getcwd(), name), 'example345')


create_file('task_5_testfile.txt', 10)
