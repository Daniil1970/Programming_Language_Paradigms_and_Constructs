class Color:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    def __str__(self) -> str:
        return self._color

    def __repr__(self) -> str:
        return "Color({!r})".format(self._color)
