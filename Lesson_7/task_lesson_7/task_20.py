# Задача №20 (Задача на словари 2)

"""
Дан текст (много строк в одном вводе) состоящий из нескольких строки.
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.

!!!Задачу необходимо решить с использованием словаря!!!
"""

dictionary = {}

num_str = int(input('Введите число строк: '))

for text in range(num_str):
    string = input('Введите строку: ', )
    for word in string:
        dictionary[word] = dictionary.get(word, 0) + 1

# Сперва мы находим максимальное значение нашего словаря
max_value = max(dictionary.values())

# Через цикл пребираем все значения и если есть одинаковые значения выведит последнее.
for key, values in dictionary.items():
    if values == max_value:
        word = key

print(dictionary[word])
