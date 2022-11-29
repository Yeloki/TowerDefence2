"""
Файл для пользовательских исключений в модуле Base
"""


class SizeValueError(Exception):

    def __init__(self, message: str = "Size value must be above zero"):
        self.message = message
        super().__init__(self.message)
