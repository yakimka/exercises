from numbers import Number


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y, self.z == other.z])

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError(
                "unsupported operand type(s)"
                f" for +: '{type(self).__name__}' and '{type(other).__name__}'")

        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError(
                "unsupported operand type(s)"
                f" for -: '{type(self).__name__}' and '{type(other).__name__}'")
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, number):
        if not isinstance(number, Number):
            raise TypeError(
                "unsupported operand type(s)"
                f" for -: '{type(self).__name__}' and '{type(number).__name__}'")

        x, y, z = self
        return Point(x * number, y * number, z * number)

    def __rmul__(self, number):
        if not isinstance(number, Number):
            raise TypeError(
                "unsupported operand type(s)"
                f" for -: '{type(number).__name__}' and '{type(self).__name__}'")

        return self * number

    def __getitem__(self, item):
        return (self.x, self.y, self.z)[item]
