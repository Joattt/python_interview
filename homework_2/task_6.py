"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        print(f'name: {self.name}')


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        print(f'name: {self.price}')


name_report = ItemDiscountReportName('табуретка', 1500)
price_report = ItemDiscountReportPrice('кушетка', 3000)

# 1
name_report.get_info()
price_report.get_info()

# 2
for obj in (name_report, price_report):
    obj.get_info()


# 3
def get_report(obj):
    obj.get_info()


get_report(name_report)
get_report(price_report)
