# АСТРАКЦИЯ (ABSTRACTION)

"""
        АСТРАКЦИЯ - это способ представить конечный продукт
        таким образом, чтобы пользователю не нужно было знать
        как именно продукт работает, но пользователь мог им
        бы легко пользоваться.

        Основная идея состоит в том, чтобы отделить способ
        использования составных объектов данных от деталей
        их реализации в виде более простых объектов.
"""


class CatPurr:
    def __init__(self):
        self.__mood_purr_map = {
            "very good": "Loud",
            "good": "Medium",
            "normal": "Soft"
        }
        self.__purr_types = {
            "Loud": "PUUUURRRR!!!!",
            "Medium": "Purrrr....Purrrr",
            "Soft": "purr....purr....purr"
        }

    def _define_purr_type_by_mood(self, mood):
        return self.__mood_purr_map.get(mood)

    def _make_purr(self, poor_type):
        return self.__purr_types.get(poor_type)

    def purr(self, mood):
        return self._make_purr(self._define_purr_type_by_mood(mood))


class Cat:
    def __init__(self):
        self.__purr_mechanism = CatPurr()
        self.__mood = "normal"

    def know_cat_feelings(self):
        print(self.__purr_mechanism.purr(self.__mood))

    def give_food(self):
        if self.__mood == "normal":
            self.__mood = "good"
        elif self.__mood == "good":
            self.__mood = "very good"
        else:
            self.__mood = "very good"


cat = Cat()
cat.know_cat_feelings()
cat.give_food()
cat.know_cat_feelings()
cat.give_food()
cat.know_cat_feelings()
cat.give_food()
cat.know_cat_feelings()
