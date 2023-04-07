'''
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
"""
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
'''

import os


def print_directory_contents(sPath):
    def get_files(sPath):
        files_list = []
        for file_or_directory in os.listdir(sPath):
            full_name = os.path.join(os.path.abspath(sPath), file_or_directory)
            if os.path.isfile(full_name):
                files_list.append((os.path.abspath(sPath), file_or_directory))
            else:
                files_list.extend(get_files(full_name))
        return files_list
    for file in get_files(sPath):
        print(file)


print_directory_contents('../../python_interview')
