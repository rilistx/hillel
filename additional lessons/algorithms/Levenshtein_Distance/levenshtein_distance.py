# РЕДАКЦИОННОЕ РАССТОЯНИЕ (РАССТОЯННИЕ ЛЕВЕНШТЕЙНА)

def distance(a, b):
    def recursion(i, j):
        if i == 0 or j == 0:
            # Если строка пустая, то растояние равняется её длине (n - вставок)
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            # Если последние символы одинаковые, просто сьедаем их
            return recursion(i - 1, j - 1)
        else:
            # Иначе считаем минимальный вариант
            return 1 + min(
                recursion(i, j - 1),  # Удаление символа
                recursion(i - 1, j),  # Вставка символа
                recursion(i - 1, j - 1)  # Замена символа
            )

    return recursion(len(a), len(b))


str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')

lev = distance(str_1, str_2)
bigger = max(len(str_1), len(str_2))
pct = ((bigger - lev) / bigger) * 100

print(
    "Первая строка: {str_1}\nВторая строка: {str_2}\
    \n==============\nРасстояние Левенштейна: {lev}\
    \nСхожесть строк: {pct} %".format(str_1=str_1,
                                      str_2=str_2,
                                      lev=lev,
                                      pct=pct)
)
