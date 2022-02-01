# ФАКТОРИАЛ ЧИСЛА С ПОМОШЬЮ РЕКУРСИИ
def factorial(number):
    if number < 0:
        return -1
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(factorial(num))
