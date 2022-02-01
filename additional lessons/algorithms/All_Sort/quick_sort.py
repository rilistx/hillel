# БЫСТРАЯ СОРТИРОВКА
def quick_sort(lis, low_idx, high_ind):
    if low_idx >= high_ind:
        return

    i, j = low_idx, high_ind
    middle_value = lis[(low_idx + high_ind) // 2]

    while i <= j:
        while lis[i] < middle_value:
            i += 1
        while lis[j] > middle_value:
            j -= 1

        if i <= j:
            lis[i], lis[j] = lis[j], lis[i]
            i, j = i + 1, j - 1

    quick_sort(lis, low_idx, j)
    quick_sort(lis, i, high_ind)


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
quick_sort(lst, 0, len(lst) - 1)
print(lst)
