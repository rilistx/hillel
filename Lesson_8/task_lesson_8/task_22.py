# Задача №22 (Написать функцию is_year_leap)

"""
Написать функцию is_year_leap, принимающую 1 аргумент — номер года,
и возвращающую True, если год високосный, и False иначе.
"""

year_leap = int(input('Введите ваш год: '))


def is_year_leap(year):
    if not year % 4 and year % 100 or not year % 400:
        return True

    else:
        return False


print(is_year_leap(year_leap))
