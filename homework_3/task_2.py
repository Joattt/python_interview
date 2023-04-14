"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они
совпадают, программа должна возвращать значение True, иначе False.
"""


def check_number(input_number):
    try:
        number = float(input_number)
        if int(number) == number:
            print('Введено целое число.')
        else:
            print('Введено дробное число.')
            left, right = input_number.split('.')
            return left == right
    except ValueError:
        print('Введено не число.')


print(check_number(input('Введите число: ')))
