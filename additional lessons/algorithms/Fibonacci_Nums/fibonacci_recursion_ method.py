# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ РЕКУРСИИ
# Последовательность: 1, 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 89, ...
def fibonacci_1(number):
    if 0 <= number <= 1:
        return number
    else:
        return fibonacci_1(number - 1) + fibonacci_1(number - 2)


def fibonacci_2(number):
    return number if 0 <= number <= 1 else fibonacci_2(number - 1) + fibonacci_2(number - 2)


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(fibonacci_1(num))
print(fibonacci_2(num))
