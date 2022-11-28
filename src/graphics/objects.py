from base import Circle, Rect, Line, Vector2
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
        self.rgba = (int(r), int(g), int(b), int(a))


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
