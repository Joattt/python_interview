"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discounted_price = self.get_price - self.get_price * (self.discount / 100)
        return f'{discounted_price}'

    def get_parent_data(self):
        print(f'name: {self.get_name}, price: {self.get_price}')


parent = ItemDiscount('табуретка', 1500)
child = ItemDiscountReport(parent.get_name, parent.get_price, 20)
child.get_parent_data()

print(child)
