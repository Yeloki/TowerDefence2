from .exceptions import SizeValueError


class Vector2:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __len__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'Vector2({self.x}, {self.y})'

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def move(self, dx: float, dy: float):
        self._x += dx
        self._y += dy


class Rect:
    def __init__(self, width: int, coords: Vector2, size: Vector2):
        self._corner_coords: Vector2 = coords
        self._size: Vector2 = size
        self._width = width

    @property
    def corner_coords(self):
        return self._corner_coords

    @property
    def size(self):
        return self._size

    def move(self, dx: float, dy: float):
        self._corner_coords.x += dx
        self._corner_coords.y += dy

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise SizeValueError()
        self._size.x = width
        self._size.y = height


class Circle:
    def __init__(self, coords: Vector2, radius: float, width: int):
        self._center = coords
        self._radius = radius
        self._width = width

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def move(self, dx: float, dy: float):
        self._center.x += dx
        self._center.y += dy

    def resize(self, radius):
        if radius < 0:
            raise SizeValueError()
        self._radius = radius


class Line:
    def __init__(self, start: Vector2, end: Vector2, width: int):
        self._start_pos = start
        self._end_pos = end
        self._width = width

    @property
    def start_pos(self):
        return self._start_pos

    @property
    def end_pos(self):
        return self._end_pos
