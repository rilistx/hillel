from random import randint


array = [3, 2, 6, 9, 7, 4, 8]


# for i, num in enumerate(array, start=1):
#     print(i, num)


# iterable = iter(array)
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))


i = 10


# def generator(num):
#     while num > 0:
#         num -= 1
#         yield num


# print(generator(i))
# it = generator(i)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


myNum_1 = 10 if 1 == 1 else 20
print(myNum_1)


myNum_2 = 10 if 1 == 2 else 20
print(myNum_2)


arr_1 = [i * 2 for i in range(1, 9)]
print(arr_1)


arr_2 = [[i + randint(1, 10) for i in range(1, 4)] for j in range(1, 4)]
print(arr_2)
