from multiprocessing import freeze_support, Manager
from game.managers import EnemiesManager, MapManager, TurretsManager, GameManager
from time import time as now

if __name__ == '__main__':
    freeze_support()
    managers = {
        'map': MapManager(),
        'enemy': EnemiesManager(),
        'turret': TurretsManager(),
        'game': GameManager(),
    }

    map_manager = managers['map']
    enemy_manager = managers['enemy']

    start = now()
    enemy_manager.call_next_wave()
    enemy_manager.call_next_wave()
    while now() - start < 10:
        pass
    enemy_manager.reset()
