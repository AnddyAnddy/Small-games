from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from src.snake.game_mechanic.coordinates import Coordinates, Position
from src.snake.game_mechanic.creator.apple_creator import AppleFactory
from src.snake.game_mechanic.creator.wall_creator import WallFactory
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.game_mechanic.playable import Playable

if TYPE_CHECKING:
    from src.snake.game_mechanic.creator.creatable import Creatable
    from src.snake.game_mechanic.game import Game


class Board:

    def __init__(self):
        self.size = 10
        self.items: set[Item] = set()
        self.player: Playable | None = None
        self.all_positions = {Position(x, y) for x in range(self.size) for y in range(self.size)}
        self.creatorFactory: dict[ItemType, Creatable] = {ItemType.APPLE: AppleFactory(), ItemType.WALL: WallFactory()}

    def _check_collisions(self, game: Game):
        items_in_collisions = group_by_position(self.items)
        for items in items_in_collisions.values():
            if len(items) > 1:
                for item in items:
                    item.interact_with(game, items)

    def update(self, game):
        self._check_collisions(game)
        for item in self.items:
            item.update(game, self.items)

    def draw(self, ui):
        for item in self.items:
            item.draw(ui)

    def add(self, item: Item):
        self.items.add(item)

    def add_player(self, player: Playable):
        self.player = player

    def remove(self, item: Item):
        self.items.remove(item)

    def available_positions(self) -> list[Coordinates]:
        taken_pos = set()
        for item in self.items:
            item_pos = item.taken_position()
            taken_pos.update(item_pos)
        return list(self.all_positions - taken_pos)

    def create(self, item_type: ItemType, **kwargs):
        item: Item = self.creatorFactory[item_type].create(available_positions=self.available_positions(), **kwargs)
        self.add(item)


def group_by_position(items: Iterable[Item]) -> dict[Coordinates, list[Item]]:
    res: dict[Coordinates, list[Item]] = {}
    for item in items:
        if item.position in res:
            res[item.position].append(item)
        else:
            res[item.position] = [item]
    return res
