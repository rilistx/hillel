# Задача №19 (Задача на словари 1)

"""
В единственной строке записан текст.
Для каждого слова из данного текста подсчитайте,
сколько раз оно встречалось в этом тексте.

!!!Задачу необходимо решить с использованием словаря!!!
"""

dictionary = {}
i = 0

while True:
    word = input('Введите текст: ')
    if word == 'end':
        break
    if word in dictionary.keys():
        dictionary[word] = dictionary.get(word, i) + 1
    else:
        dictionary[word] = dictionary.get(word, i)
    print(dictionary)

print('Ваш текст : Количество повторений(', dictionary, ')')
