import random
import copy

lst = [random.randint(10, 50) for _ in range(15)]
print(lst, id(lst))
lst[3] = 88
print(lst, id(lst))

lst1 = lst
print(lst1, id(lst1))

lst1 = lst.copy()

lst[3] = 77
print(lst, id(lst))
print(lst1, id(lst1))

lst = [[1, 2, 3, 1, 2], [4, 5], [6, 7, 8, 9]]
print(lst)
print(lst[1][1])
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=' ')
    print()

lst1 = copy.deepcopy(lst)
print(id(lst), lst)
print(id(lst1), lst1)
lst[1][1] = 88
print(lst)
print(lst1)
