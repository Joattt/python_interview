"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""


def make_dict(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    return {key: value for (key, value) in zip(keys, values)}


keys_list = [1, 2, 3, 4]
values_list = ['one', 'two', 'three']
print(make_dict(keys_list, values_list))
