from base import Circle, Rect, Line
import pygame


class DrawableCircle(Circle):
    def draw(self, screen):
        pygame.draw.circle(screen, self._color.rgba, tuple(self._center), self._radius)


class DrawableRect(Rect):
    def draw(self, screen):
        print(self.size)
        pygame.draw.rect(screen, self._color.rgba,
                         pygame.Rect(self.corner_coords.x, self.corner_coords.y, self.size.x, self.size.y),
                         width=self._width)


class DrawableLine(Line):
    def draw(self, screen):
        pygame.draw.line(screen, self._color.rgba, tuple(self._start_pos), tuple(self._end_pos), width=self._width)
