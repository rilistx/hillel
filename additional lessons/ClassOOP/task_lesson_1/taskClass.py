# ЗАДАЧА 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"


person = Person('Timi', 32)
print(person.info)

print("==================================")

# ЗАДАЧА № 2


class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Woman(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name


def God():
    Adam = Man('Adam')
    Eva = Woman('Eva')
    return [Adam, Eva]
