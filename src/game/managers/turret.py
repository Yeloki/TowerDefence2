from base import Vector2
from tools import TURRETS_MANAGER_SETTINGS as CONFIG
from tools import generate_uuid, logger


class Stat:
    STATUSES = {
        'upgraded': 1,
        'no-money': 2,
        'max': 3,
    }

    def __init__(self, base, step, max_val, cost, cost_mod):
        self.__base, self.__step, self.__max, self.__cost, self.__cost_mod = \
            base, step, max_val, cost, cost_mod

    def cost(self):
        return self.__cost

    def upgrade(self, money):
        if money < self.__cost:
            return self.STATUSES['no-money']
        if self.__base >= self.__max:
            return self.STATUSES['max']
        self.__base += self.__step
        self.__cost *= self.__cost_mod
        return self.STATUSES['upgraded']


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
        self.__uuid = generate_uuid()
        self.__pos = pos
        __config = CONFIG['turrets']['gunner']
        self.__damage = Damage(__config['damage'])
        self.__rate = Rate(__config['rate'])
        self.__range = Range(__config['range'])
        self.__enemy = None

    def find_enemy(self):
        if self.__enemy is not None:
            return

    def uuid(self):
        return self.__uuid


class Prototype:
    def __init__(self, turret_name):
        self.__uuid = generate_uuid()
        self.__pos = None
        __config = CONFIG['turrets'][turret_name]
        self.__damage = Damage(__config['damage'])
        self.__rate = Rate(__config['rate'])
        self.__range = Range(__config['range'])
        self.__turret_name = turret_name

    def attach_to_mouse_pos(self):
        pass

    def update(self):
        pass

    def get_name(self):
        return self.__turret_name

    def get_current_pos(self):
        if self.__pos is not None:
            return self.__pos
        logger.warning("Turret prototype position unknown", extra={"uuid": self.__uuid})
        raise RuntimeError("Trying to get unknown position")


class TurretsManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class TurretsManager(metaclass=TurretsManagerMeta):
    MODES = {
        'normal': 1,
        'prototype': 2,
        'selected': 3,
    }
    TURRETS = {
        "gunner": GunnerTurret,
    }

    def __init__(self):
        self.__uuid = generate_uuid()
        self.__id = 0
        self.__mode = self.MODES['normal']
        self.__turrets = {}
        self.__prototype = None

    def get_prototype(self, turret_class):
        if self.__prototype is None:
            self.__prototype = Prototype(turret_class)
        return self.__prototype

    def select_turret_class(self, name):
        pass

    def build_turret(self):
        if self.__prototype is None:
            logger.error("prototype is None, build impossible", extra={"uuid": self.__uuid})
            raise RuntimeError("Turrets manager internal error")
        turret = self.TURRETS[self.__prototype.get_name()](self.__prototype.get_current_pos())
        self.__turrets[turret.uuid()] = turret

    def get_turret_stats_by_name(self, turret_name):
        pass

    def update(self):
        pass

    def upgrade_selected(self):
        pass

    def select_turret(self, turret_uuid):
        pass

    def sell_selected(self):
        pass
