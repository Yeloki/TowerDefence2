from tools import generate_uid
from base import Rect, Circle, Vector2
from objects import Color, DrawableRect, DrawableCircle
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

    def update(self):
        pass

    def change_text(self, text: str):
        self.__text = text


class CircleButton(Button):
    def __init__(self, circle: DrawableCircle, hints: str = ""):
        super().__init__(hints)
        self.__circle = circle

    def collide(self, mouse_pos):
        return (mouse_pos[0] - self.__circle.center.x) ** 2 + (
                mouse_pos[1] - self.__circle.center.y) ** 2 <= self.__circle.radius

    def draw(self, screen):
        if self.__pressed:
            self.set_style(Color(170, 170, 170, 100))
        else:
            self.set_style(Color(250, 10, 50, 150))
        self.__circle.color = self.__style
        self.__circle.draw(screen)

class RectButton(Button):
    def __init__(self, rect: DrawableRect, hints: str = ""):
        super().__init__(hints)
        self.__rect = rect
        self.__label = None

    def collide(self, mouse_pos):
        return self.__rect.corner_coords.x <= mouse_pos[0] <= self.__rect.corner_coords.x + self.__rect.size.x and \
               self.__rect.corner_coords.y <= mouse_pos[1] <= self.__rect.corner_coords.y + self.__rect.size.y

    def set_label(self):
        self.__label = Label(self.__text, False, Color(255, 255, 255, 100), self.__rect)

    def draw(self, screen):
        if self.__pressed:
            self.set_style(Color(170, 170, 170, 100))
        else:
            self.set_style(Color(250, 10, 50, 150))
        self.__rect.color = self.__style
        self.__rect.draw(screen)
        self.__label.draw(screen)


class Header:
    def __init__(self, rect, background, exit_btn, header_label):
        self._surface = pygame.Surface(rect.size)
        self._background = background
        self.set_background(background)
        self._exit_btn = exit_btn
        self._header_label = header_label
        self.flag = False

    def set_background(self, background):
        if isinstance(background, Color):
            self._surface.fill(background.rgba)
        else:
            # Здесь должен быть код для обработки в случае если это будет картинка
            pass
        self._render()

    def _render(self):
        self._exit_btn.draw(self._surface)
        self._header_label.draw(self._surface)

    def collide(self, mouse_pos):
        x, y = self.rect.corner_coords.coord
        w, h = self.rect.size.coord
        return x <= mouse_pos[0] <= w + x and y <= mouse_pos[1] <= h + y

    def event_handler(self, event):
        if self.collide(event.pos):
            if self._exit_btn.collide(event.pos):
                return self._exit_btn.event_handler(event)

            # Связанный таск со 174 строкой
            #if event.type == pygame.MOUSEBUTTONDOWN and not self.flag:
            #    self.flag = True
            #elif self.flag and event.type == pygame.MOUSEMOTION:
            #    pass
            #

    def get_flag(self):
        return self.flag

    def draw(self, screen):
        screen.blit(self._surface, rect.corner_coords)


class Widget:
    def __init__(self, rect: Rect, header: Header, background=None):
        self.rect = rect
        self._surface = pygame.Surface(rect.size)
        self._background = None
        self._obj_list = list()
        self._header = header
        self._blocked = True

    def add_obj(self, obj):
        self._obj_list.append(obj)
        self._render()

    def set_pos(self, pos):
        self.rect.corner_coords = Vector2(pos[0], pos[1])

    def set_background(self, background):
        if isinstance(background, Color):
            self._surface.fill(background.rgba)
        else:
            # Здесь должен быть код для обработки в случае если это будет картинка
            pass
        self._render()

    def collide(self, mouse_pos):
        x, y = self.rect.corner_coords.coord
        w, h = self.rect.size.coord
        return x <= mouse_pos[0] <= w + x and y <= mouse_pos[1] <= h + y

    def collide_header(self, mouse_pos):
        return self._header.collide(mouse_pos)

    def event_handler(self, event):
        if collide(event.pos):
            # Придумать и дописать обработку перемещения при клике на заголовок
            if collide_header(event.pos):
                pass
            else:
                for obj in self._obj_list:
                    if isinstance(obj, Button):
                        return obj.event_handler(event)

    def _render(self):
        for obj in self._obj_list:
            obj.draw(self._surface)

    def draw(self, screen):
        self._render()
        screen.blit(self._surface, self.rect.corner_coords)
