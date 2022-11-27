import pygame
from base import Vector2
from tools import generate_uid


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class Window(Singleton):
    def __init__(self, size=Vector2(0, 0),
                 flags=pygame.SHOWN,
                 depth=0):
        self.__size = size
        self.__flags = flags
        self.__depth = depth
        self.__surf = pygame.display.set_mode(tuple(self.__size), self.__flags, self.__depth)
        self.__uid = generate_uid()

    def __call__(self, *args, **kwargs):
        return None

    def display(self):
        pygame.display.flip()

    def blit(self, *args):
        for i in args:
            i.draw(self.__surf)

    def pull_events(self):
        return pygame.event.get()

    def get_clock(self):
        return pygame.time.get_ticks()


if __name__ == "__main__":
    pass
