# ФАКТОРИАЛ ЧИСЛА С ПОМОШЬЮ ЦИКЛА
def factorial(number):
    res_factor = 1
    for i in range(1, number + 1):
        res_factor *= i

    return res_factor


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(factorial(num))
