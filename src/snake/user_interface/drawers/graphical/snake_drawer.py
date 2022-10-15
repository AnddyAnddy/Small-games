from src.snake.game_mechanic.items.snake import Snake
from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class SnakeDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)

    def _draw_head(self, tag, x: int, y: int):
        size = self.ui.case_size
        padding = size // 2
        upemtk.cercle(x * size + padding, y * size + padding, size // 2, remplissage="grey", tag=tag)

    def _draw_body(self, tag, x, y):
        size = self.ui.case_size

        ax, ay = x, y
        bx, by = x + 1, y + 1
        upemtk.rectangle(ax * size, ay * size, bx * size, by * size, remplissage='green', tag=tag)

    def draw(self, snake: Snake):
        tag = snake.tag
        upemtk.efface(tag)
        head_x, head_y = snake.body[0]
        self._draw_head(tag, head_x, head_y)
        for i in range(1, len(snake.body)):
            x, y = snake.body[i]
            self._draw_body(tag, x, y)
