from base import Circle, Rect, Line
import pygame


class DrawableCircle(Circle):
    def draw(self, screen):
        pygame.draw.circle(screen, self._color.rgba, tuple(self._center), self._radius)


class DrawableRect(Rect):
    def draw(self, screen):
        print(self.size)
        pygame.draw.rect(screen, self._color.rgba,
                         pygame.Rect(*self.corner_coords, *self.size),
                         width=self._width)


class DrawableLine(Line):
    def draw(self, screen):
        pygame.draw.line(screen, self._color.rgba, tuple(self._start_pos), tuple(self._end_pos), width=self._width)
