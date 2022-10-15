from __future__ import annotations

import random
from random import randrange
from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Position, Direction, Coordinates
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
        game.board.add(self.create(available_positions=game.board.available_positions()))

def get_random_free_position_fast(range_x: range, range_y: range, excluded_pos: set[Position]) -> Position | None:
    x_forward, x_backward = 0, 0
    while True:
        if x_forward >= range_x.stop and x_backward <= range_x.start:
            return None
        if not x_forward > range_x.stop:
            x_forward += 1
        if not x_backward <= range_x.stop:
            x_backward -= 1
        x = randrange(range_x.start, range_x.stop)
        y = randrange(range_y.start, range_y.stop)
        pos = Position(x, y)
        y_forward, y_backward = 0, 0
        while pos in excluded_pos:
            if y_forward >= range_y.stop and y_backward <= range_y.start:
                break
            if not y_forward > range_y.stop:
                y_forward += 1
            if not y_backward <= range_y.stop:
                y_backward -= 1
            pos_back_y = Position(x, y + y_backward)
            if pos_back_y not in excluded_pos:
                return pos_back_y
            pos_forward_y = Position(x, y + y_forward)
            if pos_forward_y not in excluded_pos:
                return pos_forward_y
