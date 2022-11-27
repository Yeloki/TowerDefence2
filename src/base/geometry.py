from graphics import Color


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

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i


class Rect:
    def __init__(self, color: Color, width: int, coords: Vector2, size: Vector2):
        self._color = color
        self._width = width
        self.corner_coords: Vector2 = coords
        self.size: Vector2 = size


class Circle:
    def __init__(self, color: Color, coords: Vector2, radius: float, width: int):
        self._color = color
        self._center_coords = coords
        self._radius = radius
        self._width = width


class Line:
    def __init__(self, color: Color, start: Vector2, end: Vector2, width: int):
        self._color = color
        self._start_pos = start
        self._end_pos = end
        self._width = width
