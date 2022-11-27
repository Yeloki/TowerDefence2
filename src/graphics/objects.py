from base import Circle, Rect, Line, Text

import pygame


class DrawableCircle(Circle):
    def draw(self, screen):
        pygame.draw.circle(screen, self.__color.rgba, self.__center, self.__radius)


class DrawableRect(Rect):
    def draw(self, screen):
        pygame.draw.rect(screen, self.__color.rgba, pygame.Rect(self.corner_coords, self.size), width=self.__width)


class DrawableLine(Line):
    def draw(self, screen):
        pygame.draw.circle(screen, self.__color.rgba, self.__start_pos, self.__end_pos, width=self.__width)


