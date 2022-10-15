from __future__ import annotations

from random import randrange
from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Position, Direction
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.ui.ui_abstract import UI

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game


class Wall(Item):
    count = 0

    def __init__(self, position: Position, tag: str):
        super().__init__(position, Direction.NONE, tag, ItemType.WALL)

    def update(self, game: Game, items: Iterable[Item]):
        pass

    def draw(self, ui: UI):
        ui.draw_item(self)

    def interact_with(self, game: Game, items: Iterable[Item]):
        print(f"Something hit {self.tag}")
        # game.remove(self)
        # game.board.add(self.create())

    @staticmethod
    def create(position: Position | None = None) -> Wall:
        if not position:
            x = randrange(1, 15)
            y = randrange(1, 15)
            position = Position(x, y)
        Wall.count += 1
        return Wall(position, f"wall_{Wall.count}")
