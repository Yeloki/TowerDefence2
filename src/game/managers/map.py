from tools import generate_uid
from tools import logger
from base import Vector2
from game.game_settings import MANAGERS_SETTINGS
from typing import Dict


class Map:
    class Road:
        def __init__(self, start, end):
            self._start: Vector2 = start
            self._end: Vector2 = end

        def __len__(self):
            return len(self._end - self._start)

    class Base:
        def __init__(self, pos: Vector2):
            self.pos: Vector2 = pos
            width = MANAGERS_SETTINGS['map']['base']['width']
            height = MANAGERS_SETTINGS['map']['base']['height']
            self.size: Vector2 = Vector2(width, height)
            self.hp: int = MANAGERS_SETTINGS['map']['base']['max_hp']

    def __init__(self, args: dict):
        self.__roads: Dict[int, Map.Road] = {}
        start = args[0]
        index = 0
        for point in args[1:]:
            self.__roads[index] = self.Road(start, point)
            start = point


class MapManager:
    GAME_MODE = 0
    EDITOR_MODE = 1

    def __init__(self):
        self.__uid = generate_uid()
        logger.info('Created map manager', extra={'uid': self.__uid})
        self.__mode = self.GAME_MODE
        self.__maps: Dict[str, dict] = {}

    def get_map(self, name):
        Map(self.__maps[name])

    def load_maps_list(self):
        pass

    def set_mode(self, mode=GAME_MODE):
        self.__mode = mode

    def get_mode(self):
        return self.__mode
