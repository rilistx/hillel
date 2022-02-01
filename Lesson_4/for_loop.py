# for

"""
for <variable> in <iterable_obj>:
    operator_1
    operator_2

operator_N

for _ in <iterable_obj>:
    operator_1
    operator_2

operator_N
"""

# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     if color == 'yellow':
#         continue
#
#     print('#', i, ' color of rainbow is ', color, sep='')
#     i += 1

# range(start, stop, step)
# 10 - 20
# range(10, 20, 2)

# stop only
# range(20)
# start = 0, step = 1

# for i in range(11, 50, 2):
#     print(i, end=' ')
#
# print()
# for i in range(50):
#     if i == 35:
#         break
#
#     print(i, end=' ')

begin = int(input('Please enter start value: '))
end = int(input('Please enter finish value: '))
suma = 0

for num in range(begin, end + 1):
    if not num % 2:
        suma += num

print('Suma:', suma)
