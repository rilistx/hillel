# Задачи №3(Немного усовершенствованая "ESCAPE символы")

"""
Написать программу, которая выводит
в консоль таблицу Escape-последовательностей:
"""

r = input('Введите слово "esc"...')

esc = 'Escape sequences:\n\
\n\
\\a \t\tBell(alert)\n\
\\b \t\tBackspace\n\
\\n \t\tNew Line\n\
\\t \t\tHorizontal tab\n\
\\  \t\tBackslash \\\n\
\\" \t\tDoubel quotation mark "\n\
\\\'\t\tSingle quotation mark \''


if 'esc' in r:
    print(esc)
else:
    print('Error Enter')

# Добавил в задачу оператор IF
