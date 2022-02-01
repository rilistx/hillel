from random import randint

lst = [randint(10, 50) for _ in range(25)]
# lst = [15, 15, 15, 16, 16, 17, 18, 19, 22, 24, 24, 26, 24, 27, 29, 29, 31, 32, 33, 35, 37, 40, 44, 48, 48]
print(lst)


def bubble_sort(my_list):
    cnt = 0
    for i in range(len(my_list) - 1):
        flag = True
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                flag = False
        cnt += 1
        if flag:
            break
    return cnt


# amount = bubble_sort(lst)
# print(lst)
# print(amount)
