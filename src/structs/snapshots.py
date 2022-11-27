from base import Vector2
from typing import List


class RoadSnapshot:
    start: Vector2
    end: Vector2
    width: int


class BaseSnapshot:
    left_up: Vector2
    size: Vector2
    hp: int


class MapSnapshot:
    size: Vector2
    base: BaseSnapshot
    roads: RoadSnapshot


class EnemySnapshot:
    hp: int
    max_hp: int
    pos: Vector2


class EnemiesManagerSnapshot:
    waves: int
    enemies: List[EnemySnapshot]


class GameSnapshot:
    map: MapSnapshot
    enemies: EnemiesManagerSnapshot
