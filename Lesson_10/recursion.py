import sys


def iteratively_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res


print(iteratively_pow(2, 5))  # 32


def recursive_pow(num, exp):
    # base case
    if exp == 0:
        return 1

    # recursive case
    return num * recursive_pow(num, exp - 1)


print(recursive_pow(2, 5))


print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


def factorial_iteratively(num):
    res = 1
    for i in range(1, num + 1):
        res *= i

    return res


print(factorial_iteratively(5))  # 120


def factorial_recursive(num):
    if num == 1:
        return 1

    return num * factorial_recursive(num - 1)


print(factorial_recursive(5))


def fibonacci_iteration(n):
    x0 = 0
    x1 = 1
    while n > 0:
        s = x0 + x1
        x0 = x1
        x1 = s
        n -= 1
    return x0


def fibonacci_recursive(n):
    # # Base case
    # if 0 <= n <= 1:
    #     return n

    # Recursive case
    return n if 0 <= n <= 1 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_iteration(10))
print(fibonacci_recursive(10))
