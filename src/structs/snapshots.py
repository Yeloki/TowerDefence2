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


class EnemiesManagerSnapshot:
    waves: int
    enemies: List[EnemySnapshot]  # or maybe Dict of id -> enemyS?


class GameSnapshot:
    map: MapSnapshot
    enemies: EnemiesManagerSnapshot
