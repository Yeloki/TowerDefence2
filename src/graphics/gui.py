from tools import generate_uid
from base import Rect, Circle, Vector2
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
    def __init__(self, hints: str = ""):
        self.__text = hints
        self.__pressed = False
        self.__style = None
        self.__pressed_style = None
        self.__uid = generate_uid()
        self.handler = None
        # flags of this class:
        self.flag: bool = False
        self.triggered: bool = False

    def collide(self, mouse_pos):
        pass

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.triggered = self.collide(event.pos)
        if event.type == pygame.MOUSEBUTTONUP and self.flag:
            self.flag = False
            if self.collide(event.pos):
                self.__pressed = True
                return self.handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.flag = True

    def set_handler(self, handler):
        self.handler = handler

    def set_style(self, image):
        if isinstance(image, Color):
            self.__style = image
        elif isinstance(image, type(pygame.image)):
            pass

    def set_pressedstyle(self, image):
        if isinstance(image, Color):
            self.__pressed_style = image
        elif isinstance(image, type(pygame.image)):
            pass

    def update(self):
        pass

    def change_text(self, text: str):
        self.__text = text


class CircleButton(Button):
    def __init__(self, circle: Circle, hints: str = ""):
        super().__init__(hints)
        self.__circle = circle

    def collide(self, mouse_pos):
        return (mouse_pos[0] - self.__circle.center.x) ** 2 + (
                mouse_pos[1] - self.__circle.center.y) ** 2 <= self.__circle.radius

    def update(self):
        if self.__pressed:
            self.set_pressedstyle(Color(170, 170, 170, 100))
        else:
            self.set_style(Color(250, 10, 50, 150))
        


class RectButton(Button):
    def __init__(self, rect: Rect, hints: str = ""):
        super().__init__(hints)
        self.__rect = rect

    def collide(self, mouse_pos):
        return self.__rect.corner_coords.x <= mouse_pos[0] <= self.__rect.corner_coords.x + self.__rect.size.x and \
               self.__rect.corner_coords.y <= mouse_pos[1] <= self.__rect.corner_coords.y + self.__rect.size.y

    def set_label(self):
        self.__label = Label(self.__text, False, Color(255, 255, 255, 100), self.__rect)


class Widget:
    def __init__(self):
        pass

    def add_button(self):
        pass

    def add_label(self):
        pass

    def set_background(self):
        pass
