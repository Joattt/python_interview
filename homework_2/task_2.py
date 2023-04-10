"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name: {self.__name}, price: {self.__price}')


parent = ItemDiscount('табуретка', 1500)
child = ItemDiscountReport(parent.__name, parent.__price)
child.get_parent_data()
