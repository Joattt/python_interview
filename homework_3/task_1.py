"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""

from os.path import abspath


def get_filename(filename):
    path = abspath(filename)
    print(path)
    full_name = path.split('\\')[-1]
    name = '.'.join(full_name.split('.')[0:-1])
    if name:
        return name
    else:
        return full_name


print(get_filename('test.py'))
