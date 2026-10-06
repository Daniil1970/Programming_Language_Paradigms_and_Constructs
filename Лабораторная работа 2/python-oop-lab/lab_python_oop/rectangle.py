from typing import Union

from .figure import Figure
from .color import Color


class Rectangle(Figure):
    _name = "Прямоугольник"

    def __init__(self, width: float, height: float, color: Union[str, Color]):
        self.width = width
        self.height = height
        self.color = color if isinstance(color, Color) else Color(color)

    @classmethod
    def name(cls) -> str:
        return cls._name

    def area(self) -> float:
        return self.width * self.height

    def __repr__(self) -> str:
        return "{}: ширина={:g}, высота={:g}, цвет={}, площадь={:.2f}".format(
            self.name(), self.width, self.height, self.color, self.area()
        )
