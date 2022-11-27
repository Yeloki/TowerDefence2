from random import randint
from game.game_settings import ENEMY_MANAGER_SETTINGS
from typing import Dict


class Enemy:
    def __init__(self, hp, speed, road_index):
        self.__hp = hp
        self.__road_index = road_index
        self.__pos = ...
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


class EnemiesManager:
    def __init__(self):
        self.__enemy_id = 0
        self.__waves_count = 1
        self.__enemies: Dict[int, Enemy] = dict()
        self.__wave_size = ENEMY_MANAGER_SETTINGS['wave-size']
        self.__enemies_type = ENEMY_MANAGER_SETTINGS['enemies']
        self.__time_of_last_wave = ...
        self.__time_between_spawn = ...
        self.__need_to_spawn = ...

    def create_enemy(self, enemy_type_index):
        curr_enemy_type = self.__enemies_type[enemy_type_index]
        curr_enemy_type['hp'] *= (1 + curr_enemy_type['hp-mod'])
        self.__enemies[self.__enemy_id] = Enemy(
            curr_enemy_type['hp'],
            curr_enemy_type['speed'],
            0  # first road index always 0
        )
        self.__enemy_id += 1

    def manual_next_wave(self):
        pass
        self.__waves_count += 1

    def auto_next_wave(self):
        self.__waves_count += 1

    def update(self, time):
        pass

    def reset(self):
        pass
