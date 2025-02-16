from langchain_core.tools import tool
from math import pi


@tool
def get_rectangle_square(length: int, width: int) -> int:
    """ Рассчитать площадь прямоугольника или квадрата.
    Args:
        length: длина
        width: ширина
    """

    return length * width


@tool
def get_circle_square(radius: int) -> int:
    """ Рассчитать площадь круга.
        Args:
            radius: радиус
        """

    return pi * (radius ** 2)


tools = [get_rectangle_square, get_circle_square]
