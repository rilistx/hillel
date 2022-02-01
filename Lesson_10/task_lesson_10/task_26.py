# Задача №26 (Конвертер чисел)

"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
В качестве параметров, функция получает десятичное число и систему счисления.
Возвращает строку - результат перевода десятичного числа.
"""


def convert_numeral_system(number, to_numeral_system=None):

    system_numeral = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if number < to_numeral_system:
        return system_numeral[number]
    else:
        return convert_numeral_system(
            number // to_numeral_system, to_numeral_system) + system_numeral[number % to_numeral_system]


num = int(input('Введите десятичное число: '))

while True:
    numeral_system = int(input('Введите любую систему счисления от 2 до 36:'))
    if numeral_system < 2 or numeral_system > 36:
        continue
    else:
        break

print(convert_numeral_system(num, numeral_system))
