from tools import generate_uid
from base import Rect, Vector2
from objects import Color
import pygame


class Label:
    def __init__(self, text: str, antialias: bool, color: Color, rect: Rect):
        self.__text = text
        self.__antialias = antialias
        self.__color = color
        self.__rect = rect
        self.__surface = pygame.Surface(rect.size)
        self.__render()
        self.__font_size = None

    def __search_size(self):
        w, h = self.__rect.size
        low = 1  # replace with min_font_size
        high = 100  # replace with max_font_size
        while True:
            mid = (high + low) // 2
            font = pygame.font.Font(None, mid)
            wc, hc = font.render(self.__text, self.__antialias, self.__color.rgba).get_rect().get_size()
            if wc == w and hc == h:
                self.__font_size = mid
                break
            elif wc > w or hc > h:
                high = mid - 1
            elif w > wc or h > hc:
                low = mid + 1

            if low > high:
                self.__font_size = mid
                break

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


class Button:
    def __init__(self, color=Color(0, 0, 0, 100)):
        self._color = color
        self._style = None
        self._triggered = False
        self._pressed = False
        self._pressed_style = None
        self._text = None
        self._uid = generate_uid()
        self.handler = None

    def collide(self, mouse_pos):
        return self.rect[0] <= mouse_pos[0] <= self.rect[2] + self.rect[0] and self.rect[1] <= mouse_pos[1] <= \
               self.rect[3] + self.rect[1]

    def event_handler(self, event):
        pass

    def set_handler(self, handler):
        self.handler = handler

    def pressed(self):
        self._pressed = True

    def update(self):
        pass


class CircleButton(Button):
    def __init__(self, circle: Circle, color=Color(0, 0, 0, 100)):
        super().__init__(color=color)
        self.circle = circle


class RectButton(Button):
    def __init__(self, rect: rect, color=Color(0, 0, 0, 100)):
        super().__init__(color=color)
        self.rect = rect


class Widget:
    def __init__(self):
        pass

    def add_button(self):
        pass

    def add_label(self):
        pass

    def set_background(self):
        pass
