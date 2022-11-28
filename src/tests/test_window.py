import pygame
from graphics import Window, DrawableRect, Color, CircleButton, DrawableCircle
from base import Vector2

window = Window()
cir = DrawableCircle(Vector2(15, 20), 40, 1, Color(255, 255, 255, 150))
but = CircleButton(cir, Color(255, 255, 255, 150), Color(100, 5, 25, 150))

while True:
    window.fill(Color(0, 0, 0, 255))
    for event in window.pull_events():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod in (512, 256):
                exit()
    window.blit(but)
    window.display()
