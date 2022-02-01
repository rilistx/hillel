
"""
    public
    protected
    private
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.cpu = cpu
        self._memory = memory
        self.__hdd_volume_1 = hdd

    def get_hdd(self):
        return self.__hdd_volume_1

    def set_hdd(self, hdd):
        self.__hdd_volume_1 = hdd


comp = Computer(2300, 16000, 500)
print(comp.cpu)
print(comp._memory)
print(comp.get_hdd())
print(dir(comp))
