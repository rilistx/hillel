# Задача №21 (Функцию arithmetic)

"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
третий - операция, которая должна быть произведена над ними.
Функция должна вернуть результат вычислений зависящий от третьего
аргумент: + сложить их; - вычесть; * умножить; / разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
"""

# Вариант решения №1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Выберете какую операцию произвести над этими числами(+, -, *, /,): ")


def arithmetic(x, y, z):
    res = 0
    if c == "+":
        res = a + b
        print(a, "+", b, "=", res)
    elif c == "-":
        res = a - b
        print(a, "-", b, "=", res)
    elif c == "*":
        res = a * b
        print(a, "*", b, "=", res)
    elif c == "/":
        res = a / b
        print(a, "/", b, "=", res)
    else:
        print("Неизвестная операция!")


arithmetic(a, b, c)

# Вариант решения №2

# def arithmetic(x, y, z):
#     res = 0
#     if c == "+":
#         res = a + b
#         return res
#     elif c == "-":
#         res = a - b
#         return res
#     elif c == "*":
#         res = a * b
#         return res
#     elif c == "/":
#         res = a / b
#         return res
#     else:
#         return "Неизвестная операция!"
#
#
# print(arithmetic(a, b, c))
