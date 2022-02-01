# УЛУЧШЕНЫЙ ЛИНЕЙНЫЙ ПОИСК (JUMP_SEARCH)
def jump_search(lis, key_value):
    length = len(lis)
    jump = int(length * 0.5)
    left, right = 0, 0
    while left < length and lis[left] <= key_value:
        right = min(length - 1, left + jump)
        if lis[left] <= key_value <= lis[right]:
            break
        left += jump
    if left >= length or lis[left] > key_value:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lis[i] <= key_value:
        if lis[i] == key_value:
            return i
        i += 1
    return -1


# Проверяем, что оно работает
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
key = int(input('Введите искомое число: '))
print(jump_search(lst, key))
