from random import randint

lst = [randint(10, 50) for _ in range(10)]
print(lst)

lst1 = [{randint(1, 10): chr(randint(40, 80))} for _ in range(10)]
print(lst1)


def func(my_lst, comparator):
    for i in range(len(my_lst) - 1):
        if comparator(my_lst[i], my_lst[i + 1]) < 0:
            print(my_lst[i], '<', my_lst[i + 1])
        elif comparator(my_lst[i], my_lst[i + 1]) > 0:
            print(my_lst[i], '>', my_lst[i + 1])
        else:
            print(my_lst[i], '=', my_lst[i + 1])


def comp1(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def comp2(a, b):
    if list(a.keys())[0] < list(b.keys())[0]:
        return -1
    elif list(a.keys())[0] > list(b.keys())[0]:
        return 1
    else:
        return 0


func(lst, comp1)
func(lst1, comp2)
