from base import Circle, Rect, Line
import pygame
from base.geometry import Vector2


class Color:
    def __init__(self, r, g, b, a):
        self.rgba = (r, g, b, a)


class DrawableCircle(Circle):

    def __init__(self, coords: Vector2, radius: float, width: int, color: Color):
        self.color = color
        super().__init__(coords, radius, width)

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.rgba, tuple(self._center), self._radius)


class DrawableRect(Rect):
    def __init__(self, width: int, coords: Vector2, size: Vector2, color=Color(0, 0, 0, 100)):
        self.color = color
        super().__init__(width, coords, size)

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color.rgba,
                         pygame.Rect(*self.corner_coords, *self.size),
                         width=self._width)


class DrawableLine(Line):
    def __init__(self, start: Vector2, end: Vector2, width: int, color=Color(0, 0, 0, 100)):
        self.color = color
        super().__init__(start, end, width)

    def set_color(self, color: Color):
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color.rgba, tuple(self._start_pos), tuple(self._end_pos), width=self._width)
