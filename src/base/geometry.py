from ..graphics.common import Color


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __len__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Rect:
    def __init__(self, left_up: Vector2, size: Vector2):
        self.left_up_corner: Vector2 = left_up
        self.size: Vector2 = size


class Circle:
    def __init__(self, depth, radius, color: Color, coords):
        self.__depth = depth
        self.__radius = radius
        self.__color = color
        self.__coords = coords


class Line:
    def __init__(self, color: Color, start, end, width: int):
        self.__color = color
        self.__start_pos = start
        self.__end_pos = end
        self.__width = width
