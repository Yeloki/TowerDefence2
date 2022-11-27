from tools import generate_uid
from base import Color, Rect

class Label:
    def __init__(self, text: str, antialias: bool, color: Color, rect: Rect):
        self.__text = text
        self.__antialias = antialias
        self.__color = color
        self.__rect = rect
        self.__surface = pygame.Surface(rect.size)
        self.__render()

    def __render(self):
        pass

    def draw(self, ):
        pass

    def set_size(self, size: Vector2):
        self.__

    def set_label(self, text):
        self.__text = text
        self.__render()


class Button:
    def __init__(self):
        self.__uid = generate_uid()
        self.__style = None

        self.__pressed = False
        self.__pressed_style = None

        self.__text = None


class Widget:
    def __init__(self):
        pass

    def add_button(self):
        pass

    def add_label(self):
        pass

    def set_backgrounf(self):
        pass
