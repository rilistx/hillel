# Задача №13 (Замена символов в строке)

"""
Дана строка. Замените в этой строке все появления буквы
`h` на букву `H`, кроме первого и последнего вхождения.
Понадобятся: срезы, функция replace().
"""

while True:
    s = input('Введите строку:')
    if s.count('h') < 3:
        continue
    else:
        first_h = s[:s.find('h') + 1]
        all_h = s[s.find('h') + 1:s.rfind('h')]
        last_h = s[s.rfind('h'):]

        s = first_h + all_h.replace('h', 'H') + last_h

        print(s)
        break
