from __future__ import annotations

import time
from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Position, Direction
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.ui.ui_abstract import UI

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game


class Spider(Item):
    count = 0

    def __init__(self, position: Position, tag: str, seconds_alive: float = 5):
        super().__init__(position, Direction.NONE, tag, ItemType.SPIDER)
        self.time_created: float = time.time()
        self.seconds_alive: float = seconds_alive

    def update(self, game: Game, items: Iterable[Item]):
        current_time = time.time()
        if self.time_created + self.seconds_alive > current_time:
            game.remove(self)

    def draw(self, ui: UI):
        ui.draw_item(self)

    def interact_with(self, game: Game, items: Iterable[Item]):
        game.remove(self)
