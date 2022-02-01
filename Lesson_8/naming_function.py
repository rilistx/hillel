# '''
# def name_function(param1, param2, ... paramN):
#     function body
#
# expression
# '''
#
#
# def print_hello():
#     print('Hello World!')
#
#
# print_hello()
#
#
# def print_text(text):
#     print(text)
#
#
# string = input('Please enter same text: ')
# print_text(string)
#
#
# def my_pow(num, exp):
#     res = num ** exp
#     return res
#
#
# x = my_pow(2, 6)
# print(x)
#
# a = int(input('Please enter a number: '))
# b = int(input('Please enter exp: '))
# x = my_pow(a, b)
# print('Result =', x)
#
# x = my_pow(3*a, b-2)
# print(x)

# x = 7
#
#
# def func():
#     # f = 0
#     global x
#     x = 12
#     print(x)
#
#
# print(x)
# x = 89
# func()
# print(x)
# x = 67
# func()
# print(x)


# def my_pow(num, exp=2):
#     print(num ** exp)
#
#
# my_pow(3, 5)
# my_pow(5)
#
#
# def func(a, b, c, d=12, e=22, f=32):
#     print(a, b, c, d, e, f)
#
#
# func(1, 2, 3)
# func(1, 2, 3, 42)
# func(1, 2, 3, 42, 52)
# func(1, 2, 3, 42, 52, 62)
#
# func(1, 2, 3, f=56)
# func(f=56, a=0, e=67, b=6, c=9, d=90)


# def func(a, b=None):
#     if b is None:
#         b = []
#
#     print(a, b)
#     b.append(a)
#     print(a, b)
#
#
# func(1)
# func(3)
# func(4)
# func(5, [8, 9, 0])
# func(3, [3])


# def func1(*args):
#     print(type(args), args)
#     for value in args:
#         print(value)
#
#
# func1(1, 2, 3, 4)
# func1()
#
#
# def func2(**kwargs):
#     print(type(kwargs), kwargs)
#
#
# func2(a=None, b=3, g=7)
