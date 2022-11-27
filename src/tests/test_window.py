import pygame

from graphics import window, DrawableRect, Color

from base import Vector2

pygame.init()
re = DrawableRect(Color(255, 0, 0), 0, Vector2(0, 640), Vector2(1280, 80))

while True:
    window.fill(Color(0, 0, 0))
    for event in window.pull_events():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod in (512, 256):
                exit()
    window.blit(re)
    window.display()
