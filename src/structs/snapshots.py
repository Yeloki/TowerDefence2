"""
DRAW QUEUE: (from first to last)
map surface
roads
base
enemies
turrets
enemies stats (hp)
particles (explosions -> projectiles)
GUI (bottom plate -> widgets)
"""
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
    roads: List[RoadSnapshot]  # draw in order of indexes: 0, 1, etc.


class EnemySnapshot:
    hp: int
    max_hp: int
    pos: Vector2
    angle: float

    def __init__(self, max_hp, hp, pos, angle):
        self.max_hp = max_hp
        self.hp = hp
        self.pos = pos
        self.angle = angle


class EnemiesManagerSnapshot:
    waves: int
    time_before_next_wave: int
    enemies: List[EnemySnapshot]  # or maybe Dict of id -> enemy?


class StatSnapshot:
    name: str
    value: int
    mult: int
    max: int
    cost: int


class GameSnapshot:
    map: MapSnapshot
    enemies: EnemiesManagerSnapshot
