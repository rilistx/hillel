# ЦИКЛИЧНЫЙ МЕТОДЫ ПЕРЕВОРОТА СТРОКИ
def flip_string(strg):
    j = len(strg) - 1
    mid = len(strg) // 2
    for i in range(mid):
        strg = strg[:i] + strg[j - i] + strg[i + 1:j - i] + strg[i] + strg[j - i + 1:]

    return strg


# Проверяем, что оно работает
string = input('Введите любую строк: ')
print(flip_string(string))
