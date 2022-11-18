import pygame as pg


class GeometryObject:
    def draw(self):
        pass

    def update(self):
        pass


class Circle(GeometryObject):
    def __init__(self, depth, radius, color, coords):
        self.__depth = depth
        self.__radius = radius
        self.__color = color
        self.__coords = coords

    def draw(self, display):
        pg.draw.circle(display, self.__color, self.__radius, self.__depth)
