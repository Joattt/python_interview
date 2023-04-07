"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму
дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
"""


def calculate_bank_deposit_plus_addition(amount, term, addition):
    def calculate_addition():
        nonlocal addition, term
        added_amount = (addition + addition * (rate / 100) * (term / 12)) * (term - 2)
        return added_amount
    product_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
    product_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
    product_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
    products_list = [product_1, product_2, product_3]
    if type(amount) != int or amount <= 0:
        return 'Неверно указана сумма вклада!'
    if term not in [6, 12, 24]:
        return 'Неверно указан срок вклада!'
    if type(addition) != int or addition < 0:
        return 'Неверно указана сумма пополнения!'
    final_amount = 0
    for product in products_list:
        if product['begin_sum'] <= amount < product['end_sum']:
            final_amount = amount
            rate = product[term]
            final_amount += amount * (rate / 100) * (term / 12)
            if addition:
                final_amount += calculate_addition()
    if not final_amount:
        return 'Подходящий продукт отсутствует.'
    return final_amount


print(calculate_bank_deposit_plus_addition(80000, 12, 5000))
