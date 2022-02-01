# ЛИНЕЙНЫЙ ПОИСК
def linear_search(lis, key_value):
    for i in range(len(lis)):
        if lis[i] == key_value:
            return i
    return -1


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
key = int(input('Введите искомое число: '))
print(linear_search(lst, key))
