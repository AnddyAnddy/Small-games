from __future__ import annotations

from typing import TYPE_CHECKING

from src.snake.game_mechanic.observers.abc_observer import Observer

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game
    from src.snake.game_mechanic.items.abc_item import Item


class LogObserver(Observer):
    def on_item_remove(self, game: Game, item: Item) -> None:
        print(f"{item.tag} {item.position} removed")
