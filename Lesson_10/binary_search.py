from random import randint


def binary_search(array, key_value, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle + 1)


lst = [randint(10, 50) for _ in range(25)]
print(lst)

lst.sort()
print(lst)

key = int(input('please enter key: '))
flag, idx = binary_search(lst, key)
print('Flag:', flag)
print('Index:', idx)

if flag:
    print('Yes, index =', idx)
else:
    print('No')
    lst.insert(idx, key)
    print(lst)
