from random import randint

size = int(input('введите количество строк: '))

lst = [[randint(10, 99) for _ in range(size)] for _ in range(size)]

tmp_lst = [0] * size
for i in range(size):
    for j in range(size):
        tmp_lst[j] += lst[i][j]

# for i in range(size):
#     for j in range(size):
#         print('{:>5}'.format(lst[i][j]), end='')
#     print()
# print()
#
# for i in range(size):
#     print('{:>5}'.format(tmp_lst[i]), end='')
#
# print()

for i in range(size - 1):
    for j in range(size - 1 - i):
        if tmp_lst[j] > tmp_lst[j + 1]:
            tmp_lst[j], tmp_lst[j + 1] = tmp_lst[j + 1], tmp_lst[j]
            for x in range(size):
                lst[x][j], lst[x][j + 1] = lst[x][j + 1], lst[x][j]

# print()
# for i in range(size):
#     for j in range(size):
#         print('{:>5}'.format(lst[i][j]), end='')
#     print()
# print()
#
# for i in range(size):
#     print('{:>5}'.format(tmp_lst[i]), end='')
# print()
# print()

for c in range(size):
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if lst[j][c] > lst[j + 1][c] if c % 2 else lst[j][c] < lst[j + 1][c]:
                lst[j][c], lst[j + 1][c] = lst[j + 1][c], lst[j][c]

print()
for i in range(size):
    for j in range(size):
        print('{:>5}'.format(lst[i][j]), end='')
    print()
print()

for i in range(size):
    print('{:>5}'.format(tmp_lst[i]), end='')
print()
print()
