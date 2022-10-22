from __future__ import annotations

import time
from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Position, Direction
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.game_mechanic.tick_handler import TickHandler
from src.snake.user_interface.ui.ui_abstract import UI

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game


class Spider(Item):
    count = 0

    def __init__(self, position: Position, tag: str, ticks_alive: int = 30):
        super().__init__(position, Direction.NONE, tag, ItemType.SPIDER)
        self.time_created: float = TickHandler.instance.ticks
        self.ticks_alive: float = ticks_alive

    def update(self, game: Game, items: Iterable[Item]):

        current_tick = TickHandler.instance.ticks
        if self.time_created + self.ticks_alive < current_tick:
            game.remove(self)

    def draw(self, ui: UI):
        ui.draw_item(self)

    def interact_with(self, game: Game, items: Iterable[Item]):
        game.remove(self)
