# x = 15

# assert x < 10, 'value more than 10'

# if not x < 10:
#     raise AssertionError('value more than 10')

# import sys
# print(sys.platform)

# assert 'linux' in sys.platform, 'This code work on Linux OS'

# assert 1 == 2, '1 not equal 2'
# assert (1 == 2, '1 not '
#                 'equal 2')

"""
try:
    operator1
    operator2
except some_exception_error:
    some code to use if appere some_exception_error

"""
# x = y = res = 0
try:
    x = int(input('Please enter first value: '))
    y = int(input('Please enter second value: '))
    res = x / y
    print(x, '/', y, '=', res)
except ZeroDivisionError as ex:
    print(ex)
    res = None
except ValueError:
    print("Value error")
else:
    print('Not error')
finally:
    print('finally')
