import dataclasses
from abc import ABC


@dataclasses.dataclass(frozen=True)
class Coordinates(ABC):
    x: int
    y: int

    def __add__(self, other: 'Coordinates') -> 'Coordinates':
        return type(self)(self.x + other.x, self.y + other.y)

    def __mul__(self, n: int) -> 'Coordinates':
        return type(self)(n * self.x, n * self.y)

    def __rmul__(self, n: int) -> 'Coordinates':
        return type(self)(n * self.x, n * self.y)

    def __sub__(self, other: 'Coordinates') -> 'Coordinates':
        return type(self)(self.x - other.x, self.y - other.y)

    def __iter__(self):
        return iter((self.x, self.y))


@dataclasses.dataclass(frozen=True)
class Position(Coordinates):
    pass


@dataclasses.dataclass(frozen=True)
class Direction(Coordinates):
    RIGHT = Coordinates(1, 0)
    LEFT = Coordinates(-1, 0)
    UP = Coordinates(0, -1)
    DOWN = Coordinates(0, 1)
    NONE = Coordinates(0, 0)
