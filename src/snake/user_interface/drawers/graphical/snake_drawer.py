from src.snake.game_mechanic.items.snake import Snake
from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class SnakeDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)
        self.first_call = False
        self.cursor = None
        self.snake_size = 0

    def _draw_head(self, tag, x: int, y: int):
        size = self.ui.case_size
        padding = size // 2
        upemtk.cercle(x * size + padding, y * size + padding, size // 2, remplissage="grey", tag=tag)

    def _draw_body(self, tag, x, y):
        size = self.ui.case_size

        ax, ay = x, y
        bx, by = x + 1, y + 1
        upemtk.rectangle(ax * size, ay * size, bx * size, by * size, remplissage='green', tag=tag)

    def _draw_full_snake(self, snake, erase: bool):
        self.snake_size = len(snake.body)
        for i, (x, y) in enumerate(snake.body):
            i_tag = f"{snake.tag}_{i}"
            if erase:
                upemtk.efface(i_tag)
            self._draw_body(i_tag, x, y)
        self.cursor = self.snake_size - 1

    def _update_runner(self, snake):
        self.cursor = self.cursor - 1 if self.cursor != 0 else len(snake.body) - 1

    def draw(self, snake: Snake):

        # initial draw
        if not self.first_call:
            self._draw_full_snake(snake, False)
            self.first_call = True
            return

        # detect a change
        if len(snake.body) != self.snake_size:
            self._draw_full_snake(snake, True)

        # erase tail, draw new head and update cursor
        else:
            upemtk.efface(f"{snake.tag}_{self.cursor}")
            x, y = snake.body[0]
            self._draw_body(f"{snake.tag}_{self.cursor}", x, y)
            self._update_runner(snake)
