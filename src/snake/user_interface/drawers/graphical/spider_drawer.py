from src.snake.game_mechanic.items.spider import Spider

from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class SpiderDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)
        self.already_drawn: set[str] = set()

    def draw(self, spider: Spider):
        if spider.tag in self.already_drawn:
            return
        self.already_drawn.add(spider.tag)
        x, y = spider.position
        size = self.ui.case_size
        padding = size // 2
        upemtk.cercle(x * size + padding, y * size + padding, size // 2, remplissage="black", tag=spider.tag)
