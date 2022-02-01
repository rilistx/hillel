# ПУЗЫРЬКОВАЯ СОРТИРОВКА
def bubble_sort(lis):
    for i in range(len(lis)):
        flag = True
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                flag = False

        if flag:
            break

    return lis


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
print(bubble_sort(lst))
