# Задача №27 (Циклический сдвиг разрядов числа)

"""
Написать функцию, принимающую ТРИ параметра и выполняющая циклически сдвиг целого числа (первый параметр)
на N разрядов (второй параметр) вправо или влево, в зависимости от значения третьего параметра функции.
Третий параметр булевский, задаёт направление сдвига (по умолчанию влево (False)).
"""


def shift(number, step, side_shift=False):
    number = str(number)
    if step < 0:
        step = abs(step)
    if side_shift:
        for i in range(step):
            number = number[-1] + number[0] + number[1:-1]
    else:
        for i in range(step):
            number = number[1:-1] + number[-1] + number[0]

    number = int(number)
    print()
    return print('Результат вашего сдвига:', number, type(number))


num = int(input('Введите любое число: '))
print(num)
steps = int(input('Введите любой шаг: '))\

while True:
    side = input(
        'Выберете сторону сдвига где:\n   '
        '0 - это сдвиг влево\n   '
        '1 - это сдвиг вправо\n   '
        '!!!Enter - по умолчанию стоит сдвиг влево!!!\n\n'
        'Ваш выбор:')

    if side == '0':
        side = False
        break
    elif side == '1':
        side = True
        break
    elif side == '':
        side = False
        break
    else:
        continue

shift(num, steps, side)
