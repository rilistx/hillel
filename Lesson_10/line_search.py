from random import randint

lst = [randint(20, 40) for _ in range(25)]
print(lst)

key = 34
for i in range(len(lst)):
    if lst[i] == key:
        print(i)
