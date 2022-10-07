from pygame.color import Color as PGColor


class Color:
    def __init__(self, *args):
        self.color = PGColor(args)
