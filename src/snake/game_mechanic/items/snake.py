from __future__ import annotations

from typing import Iterable
from typing import TYPE_CHECKING

from src.snake.game_mechanic.coordinates import Coordinates
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType

if TYPE_CHECKING:
    from src.snake.user_interface.ui.ui_abstract import UI
    from src.snake.game_mechanic.game import Game


class Snake(Item):

    def __init__(self, head: Coordinates, direction: Coordinates):
        super().__init__(head, direction, "snake", ItemType.SNAKE)
        self.body: list[Coordinates] = [head - n * direction for n in range(4)]
        self._is_dead: bool = False

    def move(self):
        head = self.body[0]
        self.position = head + self.direction
        self.body.insert(0, self.position)
        self.body.pop()

    def check_own_collision(self):
        if len(self.body) != len(set(self.body)):
            self._is_dead = True

    def _grow(self):
        second_last, last = self.body[-2:]
        new_pos = 2 * last - second_last
        self.body.append(new_pos)

    def update(self, game: Game, items: Iterable[Item]):
        self.move()
        self.check_own_collision()

    def draw(self, ui: UI):
        ui.draw_item(self)

    def interact_with(self, game: Game, items: Iterable[Item]):
        for item in items:
            match item.item_type:
                case ItemType.APPLE:
                    self._grow()
                case ItemType.WALL:
                    self._is_dead = True
                case ItemType.SPIDER:
                    self._grow()
                    self._grow()
                    self._grow()

    def is_dead(self) -> bool:
        return self._is_dead

    def taken_position(self) -> set[Coordinates]:
        return set(self.body)

    def __str__(self):
        return " - ".join(str(e) for e in self.body)
