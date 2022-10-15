from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.drawers.abc_drawer import Drawer


class Drawers:
    def __init__(self):
        self.drawers: dict[ItemType, Drawer] = {}

    def add(self, item_type: ItemType, drawer: Drawer):
        self.drawers[item_type] = drawer

    def remove(self, item_type: ItemType):
        self.drawers.pop(item_type)

    def draw(self, item: Item):
        self.drawers[item.item_type].draw(item)
