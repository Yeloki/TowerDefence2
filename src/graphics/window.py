import pygame
from base import Vector2
from tools import generate_uuid
from .common import Color
from tools.settings import SETTINGS


class WindowMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Window(metaclass=WindowMeta):

    def __init__(self):
        self.__size = Vector2(SETTINGS['window']['width'], SETTINGS['window']['height'])
        self.__surf = pygame.display.set_mode(tuple(self.__size), pygame.DOUBLEBUF)
        self.__uuid = generate_uuid()

    def fill(self, color: Color):
        self.__surf.fill(color.rgba)

    @staticmethod
    def display():
        pygame.display.flip()

    def blit(self, *args):
        for graphics_object in args:
            graphics_object.draw(self.__surf)

    @staticmethod
    def pull_events():
        return pygame.event.get()

    @staticmethod
    def get_clock():
        return pygame.time.get_ticks()

    @staticmethod
    def update(event):
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod in (512, 256):
                exit()


