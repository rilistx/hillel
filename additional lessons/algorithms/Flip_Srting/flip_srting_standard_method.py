# СТАНДАРТНЫЕ МЕТОДЫ ПЕРЕВОРОТА СТРОКИ
def flip_string(strg):
    strg = strg[::-1]
    return strg


# Проверяем, что оно работает
string = input('Введите любую строк: ')
print(flip_string(string))
