from game.game_settings import TURRETS_MANAGER_SETTINGS as CONFIG
from base.geometry import Vector2
from typing import Dict


class Stat:
    UPGRADED = 'UPGRADED'
    NO_MONEY = 'NO_MONEY'
    MAX = 'MAX'

    def __init__(self, base, step, max_val, cost, cost_mod):
        self.__base, self.__step, self.__max, self.__cost, self.__cost_mod = \
            base, step, max_val, cost, cost_mod

    def cost(self):
        return self.__cost

    def upgrade(self, money):
        if money < self.__cost:
            return self.NO_MONEY
        if self.__base >= self.__max:
            return self.MAX
        self.__base += self.__step
        self.__cost *= self.__cost_mod
        return self.UPGRADED


class Damage(Stat):
    def __init__(self, damage_config):
        super(Damage, self).__init__(**damage_config)


class Rate(Stat):
    def __init__(self, rate_config):
        super(Rate, self).__init__(**rate_config)


class Range(Stat):
    def __init__(self, range_config):
        super(Range, self).__init__(**range_config)


class GunnerTurret:
    def __init__(self, pos):
        self.__pos = pos
        __config = CONFIG['turrets']['gunner']
        self.__damage = Damage(CONFIG['damage'])
        self.__rate = Damage(CONFIG['rate'])
        self.__range = Damage(CONFIG['range'])
        self.__enemy = None

    def find_enemy(self):
        if self.__enemy is not None:
            return


class TurretsManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class TurretsManager(metaclass=TurretsManagerMeta):
    def __init__(self):
        self.__id = 0
        self.__turrets = {}

    def get_prototype(self, turret_class):
        pass

    def select_turret_class(self, name):
        pass

    def build_turret(self, name, pos):
        pass

    def get_turret_stats_by_name(self):
        pass