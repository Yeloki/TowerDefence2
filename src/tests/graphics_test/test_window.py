import pygame

from graphics import Window as window, DrawableRect, Color

from base import Vector2

pygame.init()
re = DrawableRect(1, Vector2(0, 600), Vector2(1280, 120), Color(255, 0, 0))

while True:
    window().fill(Color(0, 0, 0))
    for event in window().pull_events():
        window().update(event)
    window().blit(re)
    window().display()
