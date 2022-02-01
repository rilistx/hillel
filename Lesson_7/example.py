import random

lst = [random.randint(10, 50) for _ in range(15)]
print(lst)

k = 0

for i in range(k, len(lst) - 1):
    lst[i] = lst[i + 1]

print(lst)
lst.pop()
print(lst)

a = 7
b = a
