# НАСЛЕДОВАНИЕ (INHERITANCE - Наследуются от класса родителя)

"""
        НАСЛЕДОВАНИЕ - это принцип в программировании,
        когда классы могут быть представлены иерархической
        структурой, где потомки могут наследовать
        определённые свойства или методы своих родителей,
        а также расширять их функционал.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def namePerson(self):
        return f"Name person: {self.name}"


class Info(Person):                                  # --> НАСЛЕДУЕТ ОТ КЛАССА "PERSON" <--
    def __init__(self, name, age, growth):
        super().__init__(name)
        self.age = age
        self.growth = growth

    def infoPerson(self):
        return f"Info person:\n" \
               f"----------------------\n" \
               f"Age: {self.age}\n" \
               f"Growth: {self.growth}"


person_1 = Info("Kyrylo", 24, 188)
person_2 = Person("Igor")
print(f"Class Info: {person_1.namePerson()}")
print(person_1.infoPerson())
print()
print(f"Class Person: {person_2.namePerson()}")

print('====================================================')
print()


# --> EXAMPLE 2 <--

class Itarator:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

        return self.array


class BackItarator_1(Itarator):
    def back_itarate_1(self):
        return self.array[::-1]


array_1 = [7, 3, 4, 2, 8, 9, 5, 6, 0, 1]
array_2 = [7, 3, 4, 2, 8, 9, 5, 6, 0, 1]
array_3 = [7, 3, 4, 2, 8, 9, 5, 6, 0, 1]

arr_1 = Itarator(array_1)
arr_2 = BackItarator_1(array_2)
arr_3 = BackItarator_1(array_3)


print(arr_1.bubble_sort())
print(arr_2.back_itarate_1())

arr_3.bubble_sort()
print(arr_3.back_itarate_1())


print()
print('=========================================================================')
print()
print('МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ (ПРИМЕР)')
print()


class Company:
    def __init__(self, name):
        self.name = name

    def info_company(self):
        print(self.name)


class Car:
    def __init__(self, name_car):
        self.name_car = name_car

    def info_car(self):
        print(self.name_car)

    def view(self):
        print('This is sport Car!')


class Motor(Company, Car):
    def __init__(self, name, name_car, num_motor):
        Company.__init__(self, name)
        Car.__init__(self, name_car)
        self.num_motor = num_motor

    def full_info_motor(self):
        print(f"{self.name}\n{self.name_car}\n{self.num_motor}")


class Cuzov(Company, Car):
    def __init__(self, name, name_car, num_cuzov):
        Company.__init__(self, name)
        Car.__init__(self, name_car)
        self.num_cuzov = num_cuzov

    def full_info_cuzov(self):
        print(f"{self.name}\n{self.name_car}\n{self.num_cuzov}")


my_motor = Motor('Shell Motors', 'BMW', '0209')
my_cuzov = Motor('Shell Motors', 'BMW', 'E30')
variable = my_motor.num_motor
print(variable)
