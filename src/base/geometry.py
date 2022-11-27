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
