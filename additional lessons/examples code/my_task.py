def squared_digits_series(n):
    num = 1
    number = 0

    while n > 0:
        for j in range(num):
            n -= 1
            number += (num * 10) + 1
            if not n:
                break
        num *= 2
        if not n:
            break

    return number


print(squared_digits_series(10))
