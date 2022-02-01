# ЖАДНЫЙ АЛГОРИТМ

"""
Например: У нас есть мешок ёмкостью 10 кг. и три горки золота:
 1. вес 3 кг. цена - 1500 грн за кг.
 2. вес 5 кг. цена - 1000 грн за кг.
 3. вес 10 кг. цена - 500 грн за кг.

Нужно напонять его саммым ценным золотом, а если не помешается вся горка, то взять её часть!
"""

from copy import copy  # noqa


def greedy(my_weight):
    gold = {
        500: 10,
        1000: 5,
        1500: 3
    }

    new_gold = gold.copy()
    my_bag = {}

    while my_weight > 0:
        if len(gold) == 0:
            break
        money = max(gold.keys())
        weight = gold[money]
        gold.pop(money)
        if weight > 0:
            if my_weight > weight:
                my_bag[money] = weight
                new_gold[money] = 0
                my_weight -= weight
            else:
                my_bag[money] = my_weight
                new_gold[money] = weight - my_weight
                my_weight = 0

    return 'Осталось', new_gold, 'Поместилось', my_bag


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(greedy(num))
