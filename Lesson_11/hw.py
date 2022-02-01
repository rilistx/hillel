from string import ascii_uppercase  # noqa
# from string import digits

# 123456789


def shift_num(num, amount, direction=False):
    num = str(num)
    # while amount > 0:
    #     if direction:
    #         tmp = num[-1]
    #         for i in range(len(num)-1, 0, -1):
    #             num[i] = num[i-1]
    #         num[0] = tmp
    #     else:
    #         tmp = num[0]
    #         for i in range(len(num)-1):
    #             num[i] = num[i+1]
    #         num[-1] = tmp
    #     amount -= 1
    s1 = ''
    s2 = ''
    if direction:       # right
        s2 = num[-amount:]
        s1 = num[:-amount]
    else:               # left
        s1 = num[: amount]
        s2 = num[amount:]

    num = s2 + s1

    return num


print(shift_num(123456789, 3))
print(shift_num(123456789, 3, True))
