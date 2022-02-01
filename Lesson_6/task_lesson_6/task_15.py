# Задача №15 (Петя перешёл в другую школу)

"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось
определить своё место в строю. Помогите ему это сделать.

  -  Программа получает на вход не возрастающую последовательность натуральных чисел,
   означающих рост каждого человека в строю. После этого вводится число X – рост Пети.
   Все числа во входных данных натуральные и не превышают 200.
  -  Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с
   таким же ростом, как у Пети, то он должен встать после них.
"""

import random

num = int(input('Введите кол-во школьников в классе:'))
print('В класе', num, 'учеников.')
students_growth = [random.randint(1, 200) for i in range(num)]
students_growth.sort(reverse=True)
print('Рост каждого ученика:', students_growth)
Petya = int(input('Введите рост Пети:'))
print('Рост Пети:', Petya)

growth = 0

while growth < len(students_growth):
    if students_growth[growth] < Petya:
        students_growth.insert(growth, Petya)
        print(students_growth)
        break
    else:
        growth += 1
        continue

print('Петя с ростом', Petya, 'должен встать', growth + 1, 'в строю!')
