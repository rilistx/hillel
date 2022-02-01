
class WaterBird:
    def __init__(self, name):
        self.name = name
        print('Bird name is:', self.name)

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim fast')

    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin is ready')

    def where_is_live(self):
        print('North Pole')

    def run(self):
        print('Run fast')

    def voice(self):
        print('pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('kra-kra-kra')


penguin = Penguin('Ping')
penguin.where_is_live()
penguin.swim()
penguin.voice()
penguin.run()

print('=' * 50)

duck = Duck('Donald Duck')
duck.where_is_live()
duck.swim()
duck.voice()
duck.fly()
