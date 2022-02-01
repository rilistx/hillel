# ПОЛИМОРФИЗМ (POLYMORPHISM - Разное поведение одного и того же метода в разных классах)

"""
        ПОЛИМОРФИЗМ - разное поведение одного и того
        же метода в разных классах.

        Полиморфизм достигается путём перегрузки или
        переопределением метода.

        Таким образом достигаеться дополнительная
        гибкость программы.
"""


print("============= ПРИМЕР № 1 =============")


class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        if self.name == "dog":
            return "Bark!"
        elif self.name == "cat":
            return "Meow!"
        else:
            return "..."


dog = Animal(name="dog")
cat = Animal("cat")
spider = Animal("spider")
print(dog.voice())  # Bark!
print(cat.voice())  # Meow!
print(spider.voice())  # ...

print("============= ПРИМЕР № 2 =============")


class Car:
    def __init__(self, name):
        self.__name_speed_dict = {
            "Mercedes": 250,
            "BMW": 300
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self.__name_speed_dict.get(name, 0)

    def distance_time_on_max_speed(self, distanse):
        if not self._max_speed:
            print("No speed param specified.")
            return 0
        return distanse / self._max_speed


car_a = Car(name="BMW")
car_b = Car("Mercedes")
print(car_a.distance_time_on_max_speed(distanse=167))
print(car_b.distance_time_on_max_speed(167))

print("============= ПРИМЕР № 3 =============")


class Multiplier:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def multiply(self, variable):
        return variable * self._multiplier


multiplier_instance = Multiplier(3)
print(multiplier_instance.multiply("hello "))
print(multiplier_instance.multiply(4))
