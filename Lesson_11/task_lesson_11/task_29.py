# Задача №29 (Рисование в консоли)

"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
"""

my_empty_triangle = 'пустой треугольник'
my_filled_triangle = 'закрашеный треугольник'
my_empty_rhombus = 'пустой ромб'
my_filled_rhombus = 'закрашей ромб'
my_rhombus_50_50 = 'верхняя часть ромба закрашеная а нижняя пустая'
my_rhombus_50_25_25 = 'верхняя часть ромба закрашеная а нижняя пустая и вертикальной линией'
end = None


# Декоратор
def remain(function):
    global end

    def wrapper(num):
        global end
        result = function(num)

        print()

        while end != 1 or end != 0:
            end = input("""Выберете следующее действие:

 1. Ещё разок выбрать фигуру
 0. Завершить роботу программы

Ваше действие: """)
            if end.isdigit():
                end = int(end)
                if end == 1 or end == 0:
                    break
                elif end != 1 or end != 0:
                    print()
                    print('!!!ТАКОГО ДЕЙСТВИЯ НЕ СУЩЕСТВУЕТ!!!')
                    print()
                    continue
            else:
                print()
                print('!!!ТАКОГО ДЕЙСТВИЯ НЕ СУЩЕСТВУЕТ!!!')
                print()
                continue
        return result
    return wrapper


# 1 Пустой треугольник
@remain
def empty_triangle(num):
    for i in range(num):
        for j in range(1, 2 * num):
            if j == num - i or j == num + i or i == num - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


# 2 Закрашеный треугольник
@remain
def filled_triangle(num):
    for i in range(num):
        for j in range(1, 2 * num):
            if num - i <= j <= num + i:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


# 3 Пустой ромб
@remain
def empty_rhombus(num):
    for i in range(num):
        middle = num // 2 + num % 2
        if i < middle:
            for j in range(num):
                if j == middle - i - 1 or j == middle + i - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
        else:
            for j in range(num - 1):
                if j == i + 1 - middle or j == num - 2 - (i - middle):
                    print('* ', end='')
                else:
                    print('  ', end='')
        print()


# 4 Закрашей ромб
@remain
def filled_rhombus(num):
    for i in range(num):
        middle = num // 2 + num % 2
        if i < middle:
            for j in range(num):
                if middle - i - 1 <= j <= middle + i - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
        else:
            for j in range(num - 1):
                if i + 1 - middle <= j <= num - 2 - (i - middle):
                    print('* ', end='')
                else:
                    print('  ', end='')
        print()


# 5 Верхняя часть ромба закрашеная а нижняя пустая
@remain
def polurhombus(num):
    for i in range(num):
        middle = num // 2 + num % 2
        if i < middle:
            for j in range(num):
                if middle - i - 1 <= j <= middle + i - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
        else:
            for j in range(num - 1):
                if j == i + 1 - middle or j == num - 2 - (i - middle):
                    print('* ', end='')
                else:
                    print('  ', end='')
        print()


# 6 Верхняя часть ромба закрашеная а нижняя пустая и вертикальной линией
@remain
def vertical_rhombus(num):
    for i in range(num):
        middle = num // 2 + num % 2
        if i < middle:
            for j in range(num):
                if middle - i - 1 <= j <= middle + i - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
        else:
            for j in range(num - 1):
                if j == i + 1 - middle or j == num - 2 - (i - middle) or j == middle - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
        print()


# ТУТ НАЧАЛО ПРОГРАММЫ!!!
while True:
    if end == 0:
        print('ВЫ ЗАВЕРШИЛИ РАБОТУ ПРОГРАММЫ!')
        break
    elif end == 1:
        end = None
        continue
    else:
        print()
        figure = input("""Выберети желаемую фигуру:

  1. Пустой треугольник
  2. Закрашеный треугольник
  3. Пустой ромб
  4. Закрашей ромб
  5. Верхняя часть ромба закрашеная а нижняя пустая
  6. Верхняя часть ромба закрашеная а нижняя пустая и вертикальной линией
  0. Завершить работу программы

Введите номер указаной фигуры: """)

        print()
        if figure.isdigit():
            figure = int(figure)
            if figure == 1:
                print('Вы выбрали', my_empty_triangle)
            elif figure == 2:
                print('Вы выбрали', my_filled_triangle)
            elif figure == 3:
                print('Вы выбрали', my_empty_rhombus)
            elif figure == 4:
                print('Вы выбрали', my_filled_rhombus)
            elif figure == 5:
                print('Вы выбрали', my_rhombus_50_50)
            elif figure == 6:
                print('Вы выбрали', my_rhombus_50_25_25)
            elif figure == 0:
                end = 0
                continue
            else:
                print()
                print('!!!ВЫ ВВЕЛИ НЕ СУЩЕСТВУЮЩУЮ ФИГУРУ!!!\n    --- Попробуйте ещё раз ---')
                print()
                continue
        else:
            print()
            print('!!!ВЫ ВВЕЛИ НЕ СУЩЕСТВУЮЩУЮ ФИГУРУ!!!\n    --- Попробуйте ещё раз ---')
            print()
            continue

        print()

        while True:
            if end == 1 or end == 0:
                break
            n = input("""      Введите любое НЕ ЧЁТНОЕ НАТУРАЛЬНОЕ число!
        *** Это будет высота вашей фигуры ***

              !!!ПРЕДУПРЕЖДЕНИЕ!!!

Если вы введёте ЧЁТНОЕ число то оно увеличится на одну
единицу. НАПРИМЕР: вы ввели число 2 оно станет 3!
Или введите "0" что бы выбрать другую фугуру.

Введите ваше число: """)

            if n.isdigit():
                n = int(n)
                if n == 0:
                    print()
                    print('Вы вернулись в меню выбора фигуры.')
                    print()
                    break

                elif n > 0:
                    if not n % 2:
                        n += 1

                    print()
                    print('Высота вашей фигуры:', n)
                    print()

                    if figure == 1:
                        empty_triangle(n)
                        print()
                    elif figure == 2:
                        filled_triangle(n)
                        print()
                    elif figure == 3:
                        empty_rhombus(n)
                        print()
                    elif figure == 4:
                        filled_rhombus(n)
                        print()
                    elif figure == 5:
                        polurhombus(n)
                        print()
                    elif figure == 6:
                        vertical_rhombus(n)
                        print()
            else:
                print()
                print('!!!ВЫ ВВЕЛИ НЕ НАТУРАЛЬНОЕ ЧИСЛО!!!')
                print()
                continue
