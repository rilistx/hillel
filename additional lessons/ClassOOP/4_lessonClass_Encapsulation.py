# ИНКАПСУЛЯЦИЯ (ENCAPSULATION - Public \ Protected \ Private - это способ защитить данные)

"""
        ИНКАПСУЛЯЦИЯ - это принцип, при котором пользователь
        использует только публичную или "Интерфейсную" часть
        класса и не вникает в его внутренюю реализацию.

        Таким образом программист скрывает определённые данные,
        методы, атрибуты от последуюющих пользователей и
        разработчиков.
"""


class Computer:
    def __init__(self, cpu, memory, ssd):
        self.cpu = cpu  # --> PUBLIC <--
        self._memory = memory  # --> PROTECTED <--
        self.__ssd_volume = ssd  # --> PRIVATE <--

    # self.__ssd = sdd

    # @property                                           --> Помогает открыть доступ к PROTECTED
    # def memory(self):                                       через декоратор @PROPERTY!!!
    #     return self._memory

    def get_ssd(self):
        return self.__ssd_volume

    def set_ssd(self, ssd):
        self.__ssd_volume = ssd


comp = Computer(2300, 16000, 500)
print(comp.cpu)
print(comp._memory)
# print(comp.__ssd)                                     # --> Из за приватности так работать не будет
# print(comp._Computer__ssd)                            # --> А вот так уже будет работать
# print(dir(comp))
print(comp.get_ssd())
print(comp.set_ssd)
