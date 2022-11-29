"""
Файл для пользовательских исключений в модуле Graphics
"""


class ColorValueError(RuntimeError):
    def __init__(self, message: str = "Color must be from 0 to 255"):
        self.message = message
        super().__init__(self.message)
