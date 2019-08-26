import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return '{0.__class__.__name__}({0.radius})'.format(self)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')

        self.__radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        # S = pi * r^2
        return math.pi * self.radius ** 2
