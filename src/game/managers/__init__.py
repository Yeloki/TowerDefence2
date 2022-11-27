from .enemy import EnemiesManager
from .turret import TurretsManager
from .map import MapManager
from .game import GameManager

managers = {
    'map': MapManager(),
    'enemy': EnemiesManager(),
    'turret': TurretsManager(),
    'game': GameManager(),
}
