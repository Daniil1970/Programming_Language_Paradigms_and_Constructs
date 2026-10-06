import math
from typing import Union

from .figure import Figure
from .color import Color


class Circle(Figure):
    _name = "Круг"

    def __init__(self, radius: float, color: Union[str, Color]):
        self.radius = radius
        self.color = color if isinstance(color, Color) else Color(color)

    @classmethod
    def name(cls) -> str:
        return cls._name

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:
        return "{}: радиус={:g}, цвет={}, площадь={:.2f}".format(
            self.name(), self.radius, self.color, self.area()
        )
