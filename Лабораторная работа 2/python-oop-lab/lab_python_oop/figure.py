from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        """Вычислить площадь фигуры."""
        pass

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        """Вернуть название фигуры."""
        pass
