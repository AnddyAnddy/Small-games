from __future__ import annotations


from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.snake.game_mechanic.game import Game
    from src.snake.game_mechanic.items.abc_item import Item


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def on_item_remove(self, game: Game, item: Item) -> None:
        """
        Receive update from subject.
        """
        pass
