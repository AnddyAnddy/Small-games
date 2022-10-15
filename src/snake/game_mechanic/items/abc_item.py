from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Coordinates, Direction
from src.snake.game_mechanic.items.item_type import ItemType

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game


class Item(ABC):

    def __init__(self, position: Coordinates, direction: Coordinates, tag: str, item_type: ItemType):
        self.position = position
        self.direction = direction
        self.tag = tag
        self.item_type = item_type

    @abstractmethod
    def update(self, game: Game, items: Iterable['Item']):
        ...

    @abstractmethod
    def interact_with(self, game: Game, items: Iterable['Item']):
        ...

    @abstractmethod
    def draw(self, ui):
        ...

    def change_direction(self, new_direction: Coordinates):
        if self.direction + new_direction == Direction.NONE:
            return
        self.direction = new_direction

    def taken_position(self) -> set[Coordinates]:
        return {self.position}
