from __future__ import annotations

from threading import Timer
from typing import TYPE_CHECKING

from src.snake.game_mechanic.tick_handler import TickHandler
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.game_mechanic.observers.abc_observer import Observer

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game
    from src.snake.game_mechanic.items.abc_item import Item


class SpiderObserver(Observer):
    def on_item_remove(self, game: Game, item: Item) -> None:
        if item.item_type == ItemType.SPIDER:
            t: TickHandler = TickHandler.instance
            t.timer(15, game.board.create, item_type=ItemType.SPIDER)
