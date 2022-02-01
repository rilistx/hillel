import math


# ## TASK 1 ## #


class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):

    def __init__(self, x, y):
        super().__init__(x, y)

    def return_point(self):
        print(f'x: {self.x}, y: {self.y}')


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def return_circle(self):
        print(f'x: {self.x}, y: {self.y}, radius: {self.radius}')

    # ЗАДАЧА № 5
    def __contains__(self, value):
        return (self.x - value.x) ** 2 + (self.y - value.y) ** 2 <= self.radius ** 2


point = Point(1, 42)
circle = Circle(0, 0, 10)

point.return_point()
circle.return_circle()


print('########################################################')
# ## TASK 2 ## #


# class Circle(Shape):
#
#     def __init__(self, x, y, radius):
#         super().__init__(x, y)
#         self.radius = radius
#
#     def square(self):
#         return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def square(self):
        return self.width * self.height * round(math.sin(math.radians(self.angle)), 1)


rectangle = Rectangle(1, 0, 4, 3)
parallelogram = Parallelogram(0, 3, 7, 7, 29)

print(rectangle.square())
print(parallelogram.square())


print('########################################################')
# ## TASK 3 ## #


class Colorizer:

    COLORS = {
        'turquoise': '\033[95m',
        'pink': '\033[95m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'red': '\033[91m',
        'gray': '\033[90m',
        'END': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        print(colorizer.COLORS[self.color])

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(colorizer.COLORS['END'])


colorizer = Colorizer

with colorizer('red'):
    print('printed in red')
print('printed in default color')

with colorizer('blue'):
    print('printed in blue')
print('printed in default color')

with colorizer('turquoise'):
    print('printed in turquoise')
print('printed in default color')


print('########################################################')
# ## TASK 4 ## #


# С ИСПОЛЬЗОВАНИЕМ ГЕНЕРАТОРА YIELD
class frange:
    def __init__(self,  left, right=None, step=1):
        if step == 0:
            raise ValueError('step cannot be zero')
        if right is None:
            left, right = 0, left
        self._left = left
        self._right = right
        self._step = step

    def __iter__(self):
        while True:
            if self._step > 0:
                if self._left >= self._right:
                    return 'the end'
            else:
                if self._left <= self._right:
                    return 'the end'
            result = self._left
            self._left += self._step
            yield result


assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])

# ДОПОЛНИЛ СВОЮ ПРОВЕРКУ ДЛЯ ЛИЧНОГО УБЕЖДЕНИЕ ЧТО FLOAT РАБОТАЕТ НОРМАЛЬНО!
assert(list(frange(5.5, 2, -1.5)) == [5.5, 4, 2.5])

assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')


print('########################################################')
# ## TASK 5 ## #


# ЭТОТ КУСОК КОДА НАХОДИТЬСЯ В ПЕРВОЙ ЗАДАЧЕ

# def __contains__(self, value):
#     if (self.x - value.x) ** 2 + (self.y - value.y) ** 2 <= self.radius ** 2:
#         return True

p = Point(6, 3)
c = Circle(6, 6, 2)

print(p in c)


# ### START TASKS ### #

# ### TASK OOP ### #

# ## TASK 5 ## #

class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance_square = (self.x - point.x)**2 + (self.y - point.y)**2
        return distance_square <= self.radius**2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 42)
c = Circle(0, 0, 10)
print(c.contains(p))


print('###################################################')


# ## TASK 6 ## #

class Robot:

    def __init__(self, battery, control, material, driving_part):
        self.battery = battery
        self.control = control
        self.material = material
        self.driving_part = driving_part

    def battery_model(self):
        print(f"Battery model: {self.battery}")

    def method_of_movement(self):
        print(self.driving_part)


class SpotMini(Robot):

    def __init__(self, battery, control, material, driving_part, speed):
        super().__init__(battery, control, material, driving_part)
        self.speed = speed

    def what_can_SpotMini(self):
        print(f"Can quickly run at a speed of {str(self.speed)} km / h moving on {self.driving_part}.")


class Atlas(Robot):

    def __init__(self, battery, control, material, driving_part, vocabulary):
        super().__init__(battery, control, material, driving_part)
        self.vocabulary = vocabulary

    def what_can_Atlas(self):
        if self.vocabulary < 100:
            print(f"It knows only {str(self.vocabulary)} words so you can't talk to him.")
        elif 100 < self.vocabulary < 200:
            print(f"It knows {str(self.vocabulary)} words and already understands you a little.")
        else:
            print(f"It knows {str(self.vocabulary)} words already and can speak freely with you")


class Handle(Robot):

    def __init__(self, battery, control, material, driving_part, сarrying_capacity):
        super().__init__(battery, control, material, driving_part)
        self.сarrying_capacity = сarrying_capacity

    def what_can_Handle(self):
        print(f"Moving on {self.driving_part}, it can lift a load weighing {str(self.сarrying_capacity)} kg.")


rob1 = SpotMini('TESLA', 'Remote Control', 'plastic', '4 foods', 65)
rob2 = Atlas('LADA', 'Computer', 'plastic', '2 foods', 123)
rob3 = Handle('AMD', 'manual', 'metal', '2 wheels', 96)

rob1.what_can_SpotMini()
rob2.what_can_Atlas()
rob3.what_can_Handle()

# ### FINISH TASKS ### #
