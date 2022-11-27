import pygame
from base import Vector2
from tools import generate_uid
from tools.settings import SETTINGS


class Window:
    def __init__(self):
        self.__size = Vector2(SETTINGS['window']['width'], SETTINGS['window']['height'])
        self.__surf = pygame.display.set_mode(tuple(self.__size), pygame.DOUBLEBUF)
        self.__uid = generate_uid()

    def fill(self, color: Color):
        self.__surf.fill(color.rgba)

    def display(self):
        pygame.display.flip()

    def blit(self, *args):
        for i in args:
            i.draw(self.__surf)

    def pull_events(self):
        return pygame.event.get()

    def get_clock(self):
        return pygame.time.get_ticks()


window = Window()
