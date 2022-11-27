from base import Vector2


class RoadSnapshot:
    def __init__(self, start: Vector2, end: Vector2, width: int):
        pass


class BaseSnapshot:
    def __init__(self, left_up: Vector2, size: Vector2, hp: int):
        pass


class MapSnapshot:
    def __init__(self, size: Vector2):
        pass


class EnemySnapshot:
    def __init__(self, hp, pos, en_type):
        pass


class EnemiesManagerSnapshot:
    def __init__(self, waves):
        pass
