"""
if <condition>:
    operator_1
    operator_2

operator_3
"""

a = 45

if a > 0:
    if a != 10:
        print('A is positive')

print('End')

"""
if <condition>:
    operators_N
else:
    operators_M
"""

b = 5
if b >= 0:
    print('Number is positive')
else:
    print('Number is negative')


if b > 0:
    print('Number is positive')
elif b < 0:
    print('Number is negative')
else:
    print('Number is zero')
