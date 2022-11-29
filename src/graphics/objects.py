from base import Circle, Rect, Line, Vector2
from .exceptions import ColorValueError
import pygame


class Color:
    def __init__(self, r: [int, str], g: [int, str], b: [int, str], a: [int, str]):
        """
        all params can be introduced like string or integer
        :param r: red shade
        :param g: green shade
        :param b: blue shade
        :param a: brightness
        """
        self._r = r
        self._g = g
        self._b = b
        self._a = a

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if 0 <= value <= 255:
            self._r = value
        else:
            raise ColorValueError("Color should be from 0 to 255")

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if 0 <= value <= 255:
            self._g = value
        else:
            raise ColorValueError("Color should be from 0 to 255")

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if 0 <= value <= 255:
            self._b = value
        else:
            raise ColorValueError("Color should be from 0 to 255")

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if 0 <= value <= 255:
            self._a = value
        else:
            raise ColorValueError("Color should be from 0 to 255")

    def rgba(self) -> tuple:
        return int(self._r), int(self._g), int(self._b), int(self._a)


class DrawableCircle(Circle):

    def __init__(self, coords: Vector2, radius: float, width: int, color=Color(0, 0, 0, 255)):
        super().__init__(coords, radius, width)
        self.color = color

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.rgba, tuple(self._center), self._radius)


class DrawableRect(Rect):
    def __init__(self, width: int, coords: Vector2, size: Vector2, color=Color(0, 0, 0, 255)):
        super().__init__(width, coords, size)
        self.color = color

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color.rgba,
                         pygame.Rect(tuple(self.corner_coords), tuple(self._size)),
                         width=self._width)


class DrawableLine(Line):
    def __init__(self, start: Vector2, end: Vector2, width: int, color=Color(0, 0, 0, 100)):
        super().__init__(start, end, width)
        self.color = color

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen,
                         self.color.rgba,
                         tuple(self._start_pos),
                         tuple(self._end_pos),
                         width=self._width)
