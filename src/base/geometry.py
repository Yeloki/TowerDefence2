class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class Rect:
    def __init__(self, width: int, coords: Vector2, size: Vector2):
        self._width = width
        self.corner_coords: Vector2 = coords
        self.size: Vector2 = size


class Circle:
    def __init__(self, coords: Vector2, radius: float, width: int):
        self._center = coords
        self._radius = radius
        self._width = width


class Line:
    def __init__(self, start: Vector2, end: Vector2, width: int):
        self._start_pos = start
        self._end_pos = end
        self._width = width

    def near_point_on_vector(self, point):
        x, y = point
        x1, y1 = self._start_pos
        x2, y2 = self._end_pos
        length = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        pr = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)
        cf = pr / length
        if cf < 0:
            cf = 0
        if cf > 1:
            cf = 1
        x_res = x1 + cf * (x2 - x1)
        y_res = y1 + cf * (y2 - y1)
        return Vector2(x_res, y_res)
