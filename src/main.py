from game.managers import EnemiesManager, MapManager, TurretsManager, GameManager
from time import time as now
from graphics import InterfaceManager
import pygame

from graphics import Window as window, DrawableRect, Color

from base import Vector2

pygame.init()
re = DrawableRect(1, Vector2(0, 600), Vector2(1280, 120), Color(255, 0, 0))

if __name__ == '__main__':
    state = 'main-menu'
    InterfaceManager().use_screen('main-menu')
    while True:
        window().fill(Color(0, 0, 0))
        for event in window().pull_events():
            window().update(event)
            InterfaceManager().update(event)
        window().blit(re)
        window().blit(InterfaceManager().get_actual_screen())
        window().display()
    # while True:
    #     if state == 'main-menu':
    #         InterfaceManager().use_screen('main-menu')

    # start = now()
    # EnemiesManager().call_next_wave()
    # EnemiesManager().call_next_wave()
    # while now() - start < 30:
    #     EnemiesManager().update()
    # EnemiesManager().reset()
