import graphics_base as graph


class Circle:
    def __init__(self, depth, radius, color: graph.Color, coords):
        self.__depth = depth
        self.__radius = radius
        self.__color = color
        self.__coords = coords


class Line:
    def __init__(self, color: graph.Color, start, end, width: int):
        self.__color = color
        self.__start_pos = start
        self.__end_pos = end
        self.__width = width
