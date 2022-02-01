# Задача №33 (Развернуть словарь)

"""
Дан словарь ключами которого являются английские слова, а значениями - списки латинских слов.
Необходимо развернуть словарь. Другими словами, необходимо, на основании заданного словаря,
создать новый словарь, у которого в качестве ключей будут взяты латинские слова,
из первого словаря, а значениями будут, соответствующие им, английские слова.

d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
"""

from pprint import pprint

d = {

    'apple': ['malum', 'pomum', 'popula'],

    'fruit': ['baca', 'bacca', 'popum'],

    'punishment': ['malum', 'multa']

}

pprint(d)
print()
dict_revers = {}

for key, value in d.items():
    for element in value:
        if element not in dict_revers:
            dict_revers[element] = []

        dict_revers[element].append(key)

pprint(dict_revers)
