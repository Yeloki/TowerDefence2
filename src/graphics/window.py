import pygame
from ..base.geometry import *


class Window:
    def __init__(self, size=Vector2(0, 0),
                 flags=pygame.OPENGL | pygame.SCALED | pygame.SHOWN | pygame.DOUBLEBUF,
                 depth=0):
        self.__size = size
        self.__flags = flags
        self.__depth = depth
        self.__surf = pygame.display.set_mode(tuple(self.__size), self.__flags, self.__depth)

    def resize(self):
        pass


if __name__ == "__main__":
    a = Window(Vector2(640, 480))
