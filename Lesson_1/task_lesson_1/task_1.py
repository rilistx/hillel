# Задача №1 ("Hello World")

"""
 - Скачать и установить Python (Не забываем про установку галочки "Add python to PATH")
 - Проверить правильность установки и доступность python.Для этого в консоли (терминале)
    вводим комманду: python -V (в ответ должны увидеть соббщение Python 3.x.x - где х.х будут
    цифры указывающие на версию установленного интерпретатора)
 - Скачать и установить среду разработки (IDE) PyCharm
 - Создать первый проект.
 - Добавить в него новый python файл
 - Набрать в этом файле первую программу: print('Hello World!')
 - Запустить программу на исполнение
 - Убедиться что программа выполнилась без ошибок
"""

print('Hello World')


# Advanced calculator

num1 = float(input('Please, enter first number: '))
num2 = float(input('Please, enter second number: '))
num3 = float(input('Please, enter third number: '))

# We perform operation of adding numbers:

num = num1 + num2 + num3

# Output on display

print("Result is amounts number: " + str(num))
