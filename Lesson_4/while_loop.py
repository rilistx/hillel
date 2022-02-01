# while

"""
while <condition>:
    operator_1
    operator_2

operator_N
"""

# i = 1
# while i < 10:
#     print(i)
#     i += 1


# while True:
#     pass

# break

# i = 1
# n = int(input('Please enter a number: '))
# while i < 100:
#     if i >= n:
#         break
#
#     print(i)
#     i += 1

# num = int(input('Please enter a number: '))
# cnt = 0
# # while True:
# #     if num == 0:
# #         break
# #
# #     print(num)
# #     cnt += 1
# #     num //= 10
#
# while num != 0:
#     print(num)
#     cnt += 1
#     num //= 10
#
# print('amount:', cnt)

# num = int(input('Please enter a number: '))
# while True:
#     n = num % 10
#     # if n % 2 == 0:
#     if not (n % 2):
#        print(n)
#
#     num //= 10
#     if not num:
#         break

# continue

# while num:
#     n = num % 10
#     num //= 10
#     if n % 2:
#         continue
#
#     print(n)

# else
# a = 1
# while a != 0:
#     a = int(input('Please enter a number: '))
#     if a < 0:
#         break
#
#     print(a)
# else:
#     print('No negative value.')

a = 1
flag = False
while a != 0:
    a = int(input('Please enter a number: '))
    if a < 0:
        flag = True
        break

    print(a)


if not flag:
    print('No negative value.')
