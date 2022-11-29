from tools import generate_uid
from base import Rect, Circle, Vector2
from graphics import Color, DrawableRect, DrawableCircle
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
    def __init__(self, style: [Color, type(pygame.image)], pressed_style, handler=None):
        self._pressed = False
        self._style = style
        self._pressed_style = pressed_style
        self.handler = handler
        self._uid = generate_uid()
        self.flag: bool = False  # Кнопка нажата
        self.triggered: bool = False  # Мышка наведена на кнопку

    def collide(self, mouse_pos):
        pass

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.triggered = self.collide(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and self.flag:
            self.flag = False
            if self.collide(event.pos):
                self._pressed = True
                return self.handler
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.flag = True
        else:
            pass

    def set_handler(self, handler):
        self.handler = handler

    def draw(self, screen):
        pass


class CircleButton(Button):
    def __init__(self, circle: DrawableCircle, style, pressed_style):
        super().__init__(style, pressed_style)
        self._circle = circle

    def collide(self, mouse_pos):
        return (mouse_pos[0] - self._circle.center.x) ** 2 + (
                mouse_pos[1] - self._circle.center.y) ** 2 <= self._circle.radius

    def update_pressed(self, screen):
        if isinstance(self._pressed_style, Color):
            self._circle.set_color(self._pressed_style)
            self._circle.draw(screen)
        elif isinstance(self._pressed_style, type(pygame.image)):
            pass

    def update_unpressed(self, screen):
        if isinstance(self._style, Color):
            self._circle.color = self._style
            self._circle.draw(screen)
        elif isinstance(self._style, type(pygame.image)):
            pass

    def draw(self, screen):
        # Если нажата, рисуем нажатую, если нет, то нет
        if self._pressed:
            self.update_pressed(screen)
        else:
            self.update_unpressed(screen)


class RectButton(Button):
    def __init__(self, rect: DrawableRect, style, pressed_style, text: str = ""):
        super().__init__(style, pressed_style)
        self.__rect = rect
        self.__label = None
        self.__text = text

    def collide(self, mouse_pos):
        return self.__rect.corner_coords.x <= mouse_pos[0] <= self.__rect.corner_coords.x + self.__rect.size.x and \
               self.__rect.corner_coords.y <= mouse_pos[1] <= self.__rect.corner_coords.y + self.__rect.size.y

    def set_label(self):
        self.__label = Label(self.__text, False, Color(255, 255, 255, 100), self.__rect)

    def update_pressed(self, screen):
        if isinstance(self.__pressed_style, Color):
            self.__rect.color = self.__pressed_style
            self.__rect.draw(screen)
        elif isinstance(self.__pressed_style, type(pygame.image)):
            pass

    def update_unpressed(self, screen):
        if isinstance(self.__style, Color):
            self.__rect.color = self.__style
            self.__rect.draw(screen)
        elif isinstance(self.__style, type(pygame.image)):
            pass

    def draw(self, screen):
        if self.__pressed:
            self.update_pressed(screen)
        else:
            self.update_unpressed(screen)
        self.__label.draw(screen)

    def change_text(self, text: str):
        self.__text = text


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
            # if event.type == pygame.MOUSEBUTTONDOWN and not self.flag:
            #    self.flag = True
            # elif self.flag and event.type == pygame.MOUSEMOTION:
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
