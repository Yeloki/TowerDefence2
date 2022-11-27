from graphics import window, DrawableRect, Color

from base import Vector2, Rect

re = DrawableRect(Color(255, 255, 255, 100), 1, Vector2(0, 640), Vector2(1280, 80))

while True:
    for event in window.pull_events():
        window.blit(re)
    window.display()
