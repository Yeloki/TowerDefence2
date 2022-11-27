from tools import generate_uid
from base import Color, Rect


class Label:
    def __init__(self, text: str, antialias: bool, color: Color, rect: Rect):
        self.__text = text
        self.__antialias = antialias
        self.__color = color
        self.__rect = rect
        self.__uid = generate_uid()


class Button:
    def __init__(self):
        self.__uid = generate_uid()
        self.__style = None

        self.__pressed = False
        self.__pressed_style = None

        self.__text = None
