from random import randint

rows = int(input('введите количество строк: '))
cols = int(input('введите количество колонок: '))

lst = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]

tmp_lst = [0] * cols
for i in range(rows):
    tmp = 0
    for j in range(cols):
        tmp += lst[i][j]
        tmp_lst[j] += lst[i][j]
        print('{:>5}'.format(lst[i][j]), end='')
    print('{:>10}'.format(tmp))

print()
for i in range(cols):
    print('{:>5}'.format(tmp_lst[i]), end='')

print()
