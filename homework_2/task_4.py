"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name: {self.get_name}, price: {self.get_price}')


parent = ItemDiscount('табуретка', 1500)
child = ItemDiscountReport(parent.get_name, parent.get_price)
child.get_parent_data()

parent.set_price(2000)
child = ItemDiscountReport(parent.get_name, parent.get_price)
child.get_parent_data()
