import pygame
from common import *
from base import Vector2


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class Window(Singleton):
    def __init__(self, size=Vector2(0, 0),
                 flags=pygame.OPENGL | pygame.SCALED | pygame.SHOWN | pygame.DOUBLEBUF,
                 depth=0):
        self.__size = size
        self.__flags = flags
        self.__depth = depth
        self.__surf = pygame.display.set_mode(tuple(self.__size), self.__flags, self.__depth)

    def __call__(self, *args, **kwargs):
        return None


if __name__ == "__main__":
    a = Window(Vector2(640, 480))
