from tools import generate_uuid
from tools import logger
from base import Vector2
from tools import MAP_MANAGER_SETTINGS
from typing import Dict
from math import atan, degrees
from tools import get_game_maps
from pathlib import Path
import json


class Map:
    class Road:
        def __init__(self, start, end):
            self._start: Vector2 = start
            self._end: Vector2 = end
            self.__angle = self.__calculate_angle()

        def __len__(self):
            return len(self._end - self._start)

        def x_size(self):
            return self._end.x - self._start.x

        def y_size(self):
            return self._end.y - self._start.y

        def start(self):
            return self._start

        def end(self):
            return self._end

        def __calculate_angle(self):
            if self.x_size() == 0:
                return 90 if self.y_size() > 0 else 270
            if self.y_size() == 0:
                return 180 if self.x_size() < 0 else 0
            tan = self.y_size() / self.x_size()
            if self.x_size() > 0:
                return degrees(atan(tan)) % 360
            return (-180 + degrees(atan(tan))) % 360

        def get_angle(self):
            return self.__angle

    class Base:
        def __init__(self, pos: Vector2):
            self.pos: Vector2 = pos
            width = MAP_MANAGER_SETTINGS['map']['base']['width']
            height = MAP_MANAGER_SETTINGS['map']['base']['height']
            self.hp: int = MAP_MANAGER_SETTINGS['map']['base']['max_hp']
            self.size: Vector2 = Vector2(width, height)

    def __init__(self, args: dict):
        self.__roads: Dict[int, Map.Road] = {}
        start = Vector2(args['map'][0]['x'], args['map'][0]['y'])
        index = 0
        for point in args['map'][1:]:
            self.__roads[index] = self.Road(start, point)
            index += 1
            start = point
        self.__roads[index] = \
            self.Road(start, Vector2(args['base']['x'], args['base']['y']))
        self.__last_road_index = index

    def get_road_angle(self, road_index):
        road = self.__roads[road_index]


class MapManager:
    GAME_MODE = 0
    EDITOR_MODE = 1

    def __init__(self):
        self.__uuid = generate_uuid()
        logger.info('Created map manager', extra={'uuid': self.__uuid})
        self.__mode = self.GAME_MODE
        self.__maps: Dict[str, dict] = {}
        self.load_maps_list()

    def get_map(self, name):
        Map(self.__maps[name])

    def parse_map_from_list(self, filepath: Path):
        name = filepath.name
        file = open(filepath)
        raw_map = json.load(file)
        self.__maps[name] = raw_map

    def load_maps_list(self):
        files_list = get_game_maps()
        for filepath in files_list:
            self.parse_map_from_list(filepath)

    def set_mode(self, mode=GAME_MODE):
        self.__mode = mode

    def get_mode(self):
        return self.__mode
