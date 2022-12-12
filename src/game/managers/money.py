from tools.settings import SETTINGS


class MoneyManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MoneyManager(metaclass=MoneyManagerMeta):
    def __init__(self):
        self.__money = 0

    def add(self, count):
        if isinstance(count, int) or count < 0:
            raise ValueError("Money count in add must be positive number")
        self.__money += count

    def spend(self, count) -> bool:
        if isinstance(count, int) or count >= self.__money:
            self.__money -= count
            return True
        return False

    def balance(self):
        return self.__money

    def snapshot(self):
        return self.balance()
