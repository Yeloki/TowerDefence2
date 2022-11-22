from tools.common import generate_uid
from ..game_settings import MANAGERS_SETTINGS
from ...base import Vector2


class Map:
    class Road:
        def __init__(self, start, end):
            self.width = MANAGERS_SETTINGS['map']['road-width']
            self.start: Vector2 = start
            self.end: Vector2 = end
            self.uid = generate_uid()

        def __len__(self):
            return len(self.start - self.end)

    def __init__(self):
        self.uid = generate_uid()
        self.size_x = MANAGERS_SETTINGS['map']['field-size-x']
        self.size_y = MANAGERS_SETTINGS['map']['field-size-y']
        self.roads = []

    def import_map(self, _from):
        pass

    def export_map(self, _to):
        pass
