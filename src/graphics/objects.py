from base import Circle, Rect, Line
from graphics import Color
from base import Vector2
import pygame


class DrawableCircle(Circle):
    def draw(self, screen):
        pygame.draw.circle(screen, self.__color.rgba, self.__center, self.__radius)


class DrawableRect(Rect):
    def draw(self, screen):
        pygame.draw.rect(screen, self._color.rgba,
                         pygame.Rect(self.corner_coords.x, self.corner_coords.y, self.size.x, self.size.y),
                         width=self._width)


class DrawableLine(Line):
    def draw(self, screen):
        pygame.draw.circle(screen, self.__color.rgba, self.__start_pos, self.__end_pos, width=self.__width)
