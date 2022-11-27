from tools import generate_uid
from ..game_settings import MANAGERS_SETTINGS
from base import Vector2, Rect
from tools import logger
from typing import Tuple


class MapManager:
    class Road:
        def __init__(self, start, end):
            self.width = MANAGERS_SETTINGS['map']['road-width']
            self.start: Vector2 = start
            self.end: Vector2 = end
            self.uid = generate_uid()

        def __len__(self):
            return len(self.start - self.end)

        def snapshot(self) -> Tuple[Vector2, Vector2]:
            return self.start, self.end

    class Base:
        def __init__(self, center: Vector2):
            self.height = MANAGERS_SETTINGS['map']['base']['height']
            self.width = MANAGERS_SETTINGS['map']['base']['width']
            self.center: Vector2 = center

        def snapshot(self) -> Rect:
            left_up_x = self.center.x - self.width // 2
            left_up_y = self.center.y - self.height // 2
            left_up = Vector2(left_up_x, left_up_y)
            size = Vector2(self.width, self.height)
            return Rect(left_up, size)

    def __init__(self):
        self.uid = generate_uid()
        self.size_x = MANAGERS_SETTINGS['map']['field-size-x']
        self.size_y = MANAGERS_SETTINGS['map']['field-size-y']
        self.roads = []
        self.base = None
        logger.info(f"Map created with size: {self.size_x}, {self.size_x}",
                    # extra={'uid': self.uid}
                    )

    def import_map(self, _from):
        pass

    def export_map(self, _to):
        pass

    def snapshot(self):
        pass
