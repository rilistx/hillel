# Задача №17 (Задача на множества 1)

"""
Дан список чисел. Определите, сколько в нем встречается различных (уникальных) чисел.

  -  Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""
import random

# Вариант решения 1 (Более обширный)
lis = set(random.randint(1, 5) for lis1 in range(10))
print(lis)
print(len(set(lis)), type(lis))

# Вариант решения 2 (В одну строку)
print(len(set(random.randint(1, 5) for lis2 in range(10))))

# Вариант решения 3 (Если у нас class list)
lis = [random.randint(1, 5) for lis3 in range(10)]
print(lis)
print(len(set(lis)), type(lis))
