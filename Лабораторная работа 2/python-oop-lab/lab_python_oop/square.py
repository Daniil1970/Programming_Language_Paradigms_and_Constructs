from typing import Union

from .color import Color
from .rectangle import Rectangle


class Square(Rectangle):
    _name = "Квадрат"

    def __init__(self, side: float, color: Union[str, Color]):
        super().__init__(side, side, color)

    @classmethod
    def name(cls) -> str:
        return cls._name

    def __repr__(self) -> str:
        return "{}: сторона={:g}, цвет={}, площадь={:.2f}".format(
            self.name(), self.width, self.color, self.area()
        )
