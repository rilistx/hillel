class Car:
    def __init__(self):
        self.model = 'Mercedes'

    @staticmethod                              # --> СТАСИЧЕСКИЙ МЕТОД (Когда нет атрибутов) <--
    def what_do_your_can_car():                # --> Что бы в скобках не писать слово SELF <--
        return "Driver..."


myCar = Car()
print(myCar.model)
print(myCar.what_do_your_can_car())
