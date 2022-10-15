from __future__ import annotations

from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Position, Direction
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.ui.ui_abstract import UI

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game


class Apple(Item):
    count = 0

    def __init__(self, position: Position, tag: str):
        super().__init__(position, Direction.NONE, tag, ItemType.APPLE)

    def update(self, game: Game, items: Iterable[Item]):
        pass

    def draw(self, ui: UI):
        ui.draw_item(self)

    def interact_with(self, game: Game, items: Iterable[Item]):
        game.remove(self)
        game.board.create(self.item_type)
