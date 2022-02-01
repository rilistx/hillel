# Задача №34 (Список учеников)

"""
В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же, записать в новый файл всех учащихся в формате:

"Фамилия И.    Ср. балл"

Говорухи А.         5.83
Петров В.           4.92
Варфаломеев Г.      5.92
Тюльпанов И.        4.08
Муромцев И.         5.42
Бессмертный К.      5.5
Мухин М.            6.92
Мартынова М.        6.08
Николаев П.         5.17
Гусева Г.           5.83
Тереньтьев С.       6.42
Трердолобов С.      5.33

Выравнивание колонок - желательно!
"""

file_input = open('src.txt', encoding='utf-8')
file_output = open('dst.txt', 'w', encoding='utf-8')

file_old = file_input.readlines()

count = 0
suma = 0

# ПО СТРОЧНО ПЕРЕБРАЛ ВЕСЬ ФАЙЛ SRC.TXT
for i in file_old:
    file = i.rstrip('\n').split()
    file = [(int(file[i]) if file[i].isdigit() else file[i]) for i in range(len(file))]
    file = [file[1], file[0][0] + '.', round((sum(file[2:]) / (len(file) - 2)), 2)]
    suma += file[2]
    count += 1

    # ТУТ У МЕНЯ ПРОВЕРКА ЕСЛИ СРЕДНИЙ БАЛ УЧЕНИКА МЕНЬШЕ 5, ТО ОН ЗАПИСЫВАЕТСЯ В ПЕРЕМЕННУЮ "OOD"
    if file[2] < 5:
        file = [str(i) for i in file]
        file = ' '.join(file)
        file = file[:file.find('.') + 1] + (' ' * (20 - (file.find('.') + 2))) + file[file.find('.') + 1:]
        print(file)
    # А ЕСЛИ ТАКОГО НЕТ ТО НЕ ЗАПИСЫВАЕТ
    else:
        file = [str(i) for i in file]
        file = ' '.join(file)
        # (' ' * (20 - (file.find('.') "+ 2"))) - ОТ НАЧАЛА СТРОКИ ДО НАЧАЛА СРЕДНЕГО БАЛЛА 20 СИМВОЛОВ
        file = file[:file.find('.') + 1] + (' ' * (20 - (file.find('.') + 2))) + file[file.find('.') + 1:]

    # ТУТ Я ЗАПИСЫВАЮ ПОЛУЧИВШУЮСЯ (РЕЗУЛЬТАТ СТРОКИ) СТРОКУ В НОВЫЙ ФАЙЛ DST.TXT
    file_output.write(file + '\n')

file_input.close()
file_output.close()

print()
print('Средний балл всего класса: ', round((suma / count), 2))
