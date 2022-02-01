# СОРТИРОВКА СЛИЯНИЕМ
def merge_sort(lis):
    if len(lis) > 1:
        # Определяем середину листа
        mid = len(lis) // 2
        # Разрезаем на половины
        right = lis[mid:]
        left = lis[:mid]

        # рекурсивно продолжаем разбивать до Len(list) = 1
        merge_sort(right)
        merge_sort(left)

        # Начинаем объединять половины в один лист
        i, j, k = 0, 0, 0
        while i < len(right) and j < len(left):
            if left[j] > right[i]:
                lis[k] = right[i]
                i += 1
            else:
                lis[k] = left[j]
                j += 1
            k += 1

        # Добавляем остатки листа в конец списка
        while i < len(right):
            lis[k] = right[i]
            i += 1
            k += 1

        # добавляем остатки листа в конец списка
        while j < len(left):
            lis[k] = left[j]
            j += 1
            k += 1

    return lis


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
print(merge_sort(lst))
