
# filter(func_ref, collection)

from random import randint

lst = [randint(0, 100) for _ in range(20)]
print(lst)

odd_numbers = list(filter(lambda x: x % 2, lst))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)

# alternatively
even_numbers = list(filter(lambda x: x % 2 - 1, lst))
print(even_numbers)
