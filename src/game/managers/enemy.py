from random import randint
from tools import ENEMY_MANAGER_SETTINGS
from tools import logger, generate_uuid
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


class EnemyQueue:
    STATUSES = {
        'active': 1,
        'ended': 2,
        'error': 3,
    }

    def __init__(self, enemy_hp, enemy_speed, enemy_type, count, cooldown, enemies_map):
        self.__time_of_last_spawn = None
        self.__uuid = generate_uuid()
        self.__cooldown = cooldown
        self.__count = count
        self.__enemy_hp = enemy_hp
        self.__enemy_speed = enemy_speed
        self.__enemy_type = enemy_type
        self.__enemies_map = enemies_map
        self.__status = self.STATUSES['active']

    def start(self):
        self.__time_of_last_spawn = now()

    def update(self):
        if self.__time_of_last_spawn is None:
            logger.error('Enemy queue was not started',
                         extra={'uuid': self.__uuid})
            self.__status = 'error'
            return self.__status

        if self.__count == 0 and self.__status == self.STATUSES['active']:
            self.__status = self.STATUSES['ended']
            return self.__status

        if now() - self.__time_of_last_spawn > self.__cooldown:
            uuid = generate_uuid()
            logger.info(f'Created enemy with type: {self.__enemy_type}',
                        extra={'uuid': uuid})
            self.__enemies_map[uuid] = Enemy(self.__enemy_hp, self.__enemy_speed, self.__enemy_type)
            self.__time_of_last_spawn = now()
            self.__count -= 1

        return self.__status

    def get_uuid(self):
        return self.__uuid


class EnemiesManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class EnemiesManager(metaclass=EnemiesManagerMeta):
    def __init__(self):
        self.__waves_count = 0
        self.__wave_size = ENEMY_MANAGER_SETTINGS['wave-size']
        self.__enemies_type = ENEMY_MANAGER_SETTINGS['enemies']
        self.__time_of_last_wave = now()
        self.__time_between_spawn = ENEMY_MANAGER_SETTINGS['time-between-enemies']
        self.__time_between_waves = ENEMY_MANAGER_SETTINGS['time-between-waves']
        self.__enemy_queues = {}
        self.__enemies = {}
        self.__queues_for_remove = set()

    def __next_wave(self, enemy_type_index):
        curr_enemy_type = self.__enemies_type[enemy_type_index]
        hp = curr_enemy_type['hp'] * (1 + curr_enemy_type['hp-mod']) ** self.__waves_count
        speed = curr_enemy_type['speed']
        name = curr_enemy_type['name']

        queue = EnemyQueue(hp, speed, name,
                           self.__wave_size,
                           self.__time_between_spawn,
                           self.__enemies)
        queue.start()
        self.__enemy_queues[queue.get_uuid()] = queue
        self.__waves_count += 1

    def call_next_wave(self):
        curr_type = randint(0, len(self.__enemies_type) - 1)
        self.__next_wave(curr_type)
        self.__time_of_last_wave = now()

    def update(self):
        if now() - self.__time_of_last_wave > self.__time_between_waves:
            self.call_next_wave()

        for queue in self.__enemy_queues.values():
            status = queue.update()
            if status == EnemyQueue.STATUSES['ended'] or status == EnemyQueue.STATUSES['error']:
                self.__queues_for_remove.add(queue.get_uuid())

        for uuid in self.__queues_for_remove:
            self.__enemy_queues.pop(uuid)
        self.__queues_for_remove.clear()

    def reset(self):
        self.__enemies.clear()
        self.__enemy_queues.clear()
        self.__waves_count = 1

        self.__time_of_last_wave = now()
