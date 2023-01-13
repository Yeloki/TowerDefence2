import pygame

from base import Rect
from tools import generate_uuid, logger, get_screens_dir
from .common import Color
from .window import Window


class Label:
    def __init__(self, text: str, antialias: bool, color: Color, rect: Rect):
        self.__uuid = generate_uuid()

        self.__text = text
        self.__antialias = antialias
        self.__color = color
        self.__rect = rect
        self.__surface = pygame.Surface(rect.size)
        self.__render()
        self.__font_size = None

    def __search_size(self):
        w, h = self.__rect.size
        mn = 1  # replace with min_font_size
        mx = 100  # replace with max_font_size
        while True:
            mid = (mx + mn) // 2
            font = pygame.font.Font(None, mid)
            wc, hc = font.render(self.__text, self.__antialias, self.__color.rgba).get_rect().get_size()
            if wc == w and hc == h:
                self.__font_size = mid
                break
            elif wc > w or hc > h:
                mx = mid - 1
            elif w > wc or h > hc:
                mn = mid + 1
            if mn > mx:
                self.__font_size = mid
                break
        logger.info(f'Setting up font size {str(self.__font_size)} for label', extra={"uuid": self.__uuid})

    def __render(self):
        self.__search_size()
        font = pygame.font.Font(None, self.__font_size)
        text = font.render(self.__text, self.__antialias, self.__color.rgba)
        self.__surface.blit(text, (0, 0))

    def draw(self, screen):
        screen.blit(self.__surface, self.__rect.corner_coords)

    def set_rect(self, rect: Rect):
        self.__rect = rect
        self.__render()

    def set_label(self, text):
        self.__text = text
        self.__render()


class ButtonStyle:
    def __init__(self, style_params):
        self.__uuid = generate_uuid()
        self.__current = 'common'
        self.__type = style_params['type']
        if self.__type == 'color':
            self.__common = Color(*map(int, style_params['common'].split()))
            self.__hover = Color(*map(int, style_params['hover'].split()))
            self.__clicked = Color(*map(int, style_params['clicked'].split()))
            logger.info('Button style created', extra={'uuid': self.__uuid})
        else:
            logger.error("Unknown style type", extra={'uuid': self.__uuid})
            pass  # feature request: add buttons from image supporting

    def get_style(self):
        if self.__current == 'common':
            return self.__type, self.__common
        elif self.__current == 'hover':
            return self.__type, self.__hover
        elif self.__current == 'clicked':
            return self.__type, self.__clicked
        logger.error(f'Unknown button style type {str(self.__type)}', extra={"uuid": self.__uuid})
        raise RuntimeError("ButtonStyle internal error")


class Button:
    def __init__(self, button_settings):
        self.__uuid = generate_uuid()
        self.__id = None

        self.__style = None
        self.__pressed = False
        self.__pressed_style = None
        self.__text = None
        self.__uuid = generate_uuid()

    def pressed(self):
        pass


class CircleButton(Button):
    pass


class RectButton(Button):
    pass


class Widget:
    def __init__(self):
        pass

    def add_button(self):
        pass

    def add_label(self):
        pass

    def set_background(self):
        pass


class Screen:
    def __init__(self, path):
        self.__uuid = generate_uuid()
        self.__buttons = {}
        self.__labels = {}
        self.__objects = {}
        self.__widgets = {}
        self.__objects = {}
        self.__background = None

    def draw(self, screen):
        for obj in self.__objects:
            if hasattr(obj, 'draw'):
                obj.draw(screen)

    def update(self, event):
        pass


class InterfaceManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class InterfaceManager(metaclass=InterfaceManagerMeta):
    def __init__(self):
        self.__uuid = generate_uuid()
        self.screens = {}
        self.current_screen = None
        self.load_screens()

    def load_screens(self):
        screens_dir = get_screens_dir()
        logger.info(screens_dir, extra={'uuid': self.__uuid})

    def use_screen(self, screen_name):
        self.current_screen = screen_name

    def update(self, event):
        for screen in self.screens.values():
            screen.update(event)

    def get_actual_screen(self):
        if self.current_screen is None:
            logger.error('You must set up screen before using it')
        return self.screens[self.current_screen]
