from random import randint
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import SyncManager
from multiprocessing.sharedctypes import Value
from game.game_settings import ENEMY_MANAGER_SETTINGS
from structs.snapshots import EnemiesManagerSnapshot, EnemySnapshot
from tools import logger, generate_uid
from base import Vector2
from time import time as now


class Enemy:
    def __init__(self, hp, speed, enemy_type):
        self.__max_hp = hp
        self.__hp = hp
        self.__road_index = 0
        self.__enemy_type = enemy_type
        self.__pos = ...
        self.__angle = ...
        self.__speed = speed

    def move(self):
        pass

    def snapshot(self):
        return EnemySnapshot(self.__max_hp, self.__hp, self.__pos, self.__angle)

    def next_road(self):
        pass

    def give_damage(self):
        pass

    def take_damage(self, damage) -> bool:
        """
        take damage)
        :param damage: damage to enemy
        :return: true if enemy die else false
        """
        self.__hp -= damage
        return self.__hp <= 0


SyncManager.register('Enemy', Enemy)


def _enemy_queue(uid,
                 enemy_hp, enemy_speed, enemy_type,
                 count, cooldown,
                 enemies_map,
                 curr_id: Value,
                 lock: Lock):
    logger.info(f'Successfully created enemy queue with enemies type: {enemy_type}',
                extra={'uid': uid})
    __time_of_last_spawn = now()
    while count > 0:
        if now() - __time_of_last_spawn > cooldown:
            lock.acquire()
            _id = curr_id.value
            curr_id.value += 1
            lock.release()
            enemy = Manager().Enemy(enemy_hp, enemy_speed, enemy_type)
            enemies_map[_id] = enemy
            count -= 1
            logger.info('enemy spawned', extra={'uid': uid})
            __time_of_last_spawn = now()
    logger.info(f'Wave of {enemy_type} was ended',
                extra={'uid': uid})


class EnemiesManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class EnemiesManager(metaclass=EnemiesManagerMeta):
    def __init__(self):
        self.__lock = Manager().Lock()
        self.__enemy_id = Value('i', 0)
        self.__waves_count = 0
        self.__manager = Manager()
        self.__enemies = self.__manager.dict()
        self.__wave_size = ENEMY_MANAGER_SETTINGS['wave-size']
        self.__enemies_type = ENEMY_MANAGER_SETTINGS['enemies']
        self.__time_of_last_wave = now()
        self.__time_between_spawn = ENEMY_MANAGER_SETTINGS['time-between-enemies']
        self.__time_between_waves = ENEMY_MANAGER_SETTINGS['time-between-waves']
        self.__enemy_queues = {}

    def __next_wave(self, enemy_type_index):
        curr_enemy_type = self.__enemies_type[enemy_type_index]
        hp = curr_enemy_type['hp'] * (1 + curr_enemy_type['hp-mod']) ** self.__waves_count
        speed = curr_enemy_type['speed']
        name = curr_enemy_type['name']
        uid = generate_uid()
        p = Process(target=_enemy_queue, args=(uid, hp, speed, name,
                                               self.__wave_size,
                                               self.__time_between_spawn,
                                               self.__enemies,
                                               self.__enemy_id,
                                               self.__lock))
        p.start()
        self.__enemy_queues[uid] = p
        self.__waves_count += 1

    def __erase_done_processes(self):
        for key in self.__enemy_queues.keys():
            if not self.__enemy_queues[key].is_alive():
                del self.__enemy_queues[key]

    def call_next_wave(self):
        self.__erase_done_processes()
        curr_type = randint(0, len(self.__enemies_type) - 1)
        self.__next_wave(curr_type)

    def update(self):
        if now() - self.__time_of_last_wave > self.__time_between_waves:
            self.call_next_wave()
            self.__time_of_last_wave = now()

    def snapshot(self):
        snapshot = EnemiesManagerSnapshot()
        snapshot.waves = self.__waves_count
        snapshot.time_before_next_wave = self.__time_of_last_wave - self.__time_between_waves
        snapshot.enemies = []
        for enemy in self.__enemies:
            snapshot.enemies.append(enemy.snapshot())
        return snapshot

    def reset(self):
        for uid, process in self.__enemy_queues.items():
            if process.is_alive():
                process.kill()
                logger.info('Successfully killed enemy queue', extra={'uid': uid})
        self.__enemies.clear()
        self.__enemy_queues.clear()
        self.__enemy_id.value = 0
        self.__waves_count = 1
        try:
            self.__lock.release()
        except RuntimeError:
            pass
        self.__time_of_last_wave = now()
