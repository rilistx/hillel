# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ ЦИКЛА
# Последовательность: 1, 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 89, ...
def fibonacci_1(number):
    n = None
    n1 = n2 = 1
    print(n1, n2, end=' ')

    while number - 2 > 0:
        n = n1 + n2
        n1 = n2
        n2 = n
        print(n, end=' ')
        number -= 1


def fibonacci_2(number):
    n = None
    n1 = n2 = 1
    print(n1, n2, end=' ')

    for _ in range(2, num):
        n = n1 + n2
        n1 = n2
        n2 = n
        print(n, end=' ')


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
fibonacci_1(num)
print()
fibonacci_2(num)
