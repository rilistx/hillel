# import sys

#              Оператор обработки ошибок работающий в режиме откладки
# --> НИ В КОЕМ СЛУЧАЕ НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ ЭТОТ ОПЕРАТОР В РАБОЧЕЙ ПРОГРАММЕ <--

# ASSERT - принимает два параметра (Условие, Сообщение)

x = 5

assert x < 10, "Value more then 10"

# ASSERT можно заменить оператором RAISE в рабочей программе!

y = 15

if y < 10:
    raise AssertionError("Value more then 10")


# Используемая Операционная Система!
# print(sys.platform)

# assert "linux" in sys.platform, "This code using only on Linux OS"


"""
    try:
        operator_1
        operator_2
        operator_N

    except some_exception_error:
        some code to use if appear some exception error
"""

num_1 = num_2 = res = 0

try:
    num_1 = int(input("Please enter first number..."))
    num_2 = int(input("Please enter second number..."))

    res = num_1 / num_2

except ZeroDivisionError as ex:
    print("--------------")
    print(str(ex).capitalize(), "is not possible!")

except ValueError as ex:
    print("--------------")
    print("ValueError:", str(ex).capitalize())


#     Это НЕ ОБЯЗАТЕЛЬНЫЙ блок!!!
#     Блок ELSE выполниться в том случаи если ошибок не произошло в блоке EXCEPT!
#     Но если ошибка произошла то блок ELSE выполняться не будет

else:
    print("--------------")
    print(num_1, "/", num_2, "=", res)


#     Это НЕ ОБЯЗАТЕЛЬНЫЙ блок!!!
#     Данный блок FINALLY выполниться в любом случаи (если будет или не будет вызвана ошибка)

finally:
    print("--------------")
    print("       ### FINALLY ###\n"
          "Этот блок выполняеться всегда")
