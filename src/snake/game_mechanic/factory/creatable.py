from typing import Protocol

from src.snake.game_mechanic.coordinates import Coordinates, Position
from src.snake.game_mechanic.items.abc_item import Item


class Creatable(Protocol):
    def create(self, available_positions: list[Coordinates] = None, forced_position: Position = None) -> Item:
        ...
