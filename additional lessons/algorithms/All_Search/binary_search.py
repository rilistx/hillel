# БИНАРНЫЙ ПОИСК
def binary_search(lis, key_value):
    low = 0
    high = len(lis) - 1

    middle = (low + high) // 2
    while lis[middle] != key_value and low <= high:
        if lis[middle] < key_value:
            low = middle + 1
        else:
            high = middle - 1

        middle = (low + high) // 2

    return middle if not (low > high) else -1


# Проверяем, что оно работает
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
key = int(input('Введите искомое число: '))
print(binary_search(lst, key))
