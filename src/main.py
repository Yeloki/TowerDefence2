from multiprocessing import freeze_support, Manager
from game.managers import EnemiesManager, MapManager, TurretsManager, GameManager
from time import time as now

if __name__ == '__main__':
    freeze_support()

    start = now()
    EnemiesManager().call_next_wave()
    EnemiesManager().call_next_wave()
    while now() - start < 10:
        pass
    EnemiesManager().reset()
