from graphics import Window, DrawableRect, Color
from tools.settings import SETTINGS
from base import Vector2, Rect

a = Window(Vector2(SETTINGS["window"]["width"], SETTINGS["window"]["height"]))
re = DrawableRect(Color(255, 255, 255, 100), 1, Vector2(0, 640), Vector2(1280, 80))

while True:
    for event in Window().pull_events():
        a.blit(re)
    Window().display()
