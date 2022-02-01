# Задача №30 (Инверсия строки)

"""
Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, и B,
соответственно, на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате
применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA

Использовать циклы и оператор IF запрещено.
"""


def string_replace(strg=''):
    strg = strg.replace('A', 'a')
    strg = strg.replace('B', 'A')
    strg = strg.replace('a', 'B')
    return strg


print(string_replace('AABABBAABBBAB'))
