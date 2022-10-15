from src.snake.game_mechanic.board import Board
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.observers.abc_observer import Observer
from src.snake.user_interface.ui.ui_abstract import UI


class Game:
    def __init__(self, ui: UI.__class__, *args, **kwargs):
        self.board: Board = Board()
        self.ui: UI = ui(self.board, *args, **kwargs)
        self._observers: list[Observer] = []

    def _check_game_over(self) -> bool:
        """Return True when the game is over, e.g. it has a winner or there is no more move to play."""
        return self.board.player.is_dead()

    def remove(self, item: Item):
        self.board.remove(item)
        self.notify_on_item_remove(item)

    def main_loop(self):
        while True:
            self.ui.display()
            self.ui.play(self.board.player)
            self.board.update(self)
            self.ui.refresh()
            if self._check_game_over():
                return

    def attach(self, observer: Observer):
        assert observer is not None
        self._observers.append(observer)

    def dettach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_on_item_remove(self, item: Item):
        for obs in self._observers:
            obs.on_item_remove(self, item)
