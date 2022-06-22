from src.tictactoe.game_mechanic.board import Board
from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.lib import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class HandleDrawing:
    def __init__(self, board_size, window_size=0, background_size=450):
        self.window_size = window_size
        self.background_size = background_size
        self.case_size = background_size // board_size
        self.start_background = (self.window_size - self.background_size) // 2
        self.end_background = self.window_size - self.start_background
        self.draw_grid()

    def draw_grid(self):
        upemtk.rectangle(self.start_background, self.start_background, self.end_background, self.end_background,
                         epaisseur=5, tag="background_grid")
        # Vertical
        upemtk.ligne(self.start_background + self.case_size, self.start_background,
                     self.start_background + self.case_size, self.end_background, epaisseur=5,
                     tag="background_grid")
        upemtk.ligne(self.start_background + 2 * self.case_size, self.start_background,
                     self.start_background + 2 * self.case_size, self.end_background, epaisseur=5,
                     tag="background_grid")
        # Horizontal
        upemtk.ligne(self.start_background, self.start_background + self.case_size, self.end_background,
                     self.start_background + self.case_size, epaisseur=5, tag="background_grid")
        upemtk.ligne(self.start_background, self.start_background + 2 * self.case_size, self.end_background,
                     self.start_background + 2 * self.case_size, epaisseur=5,
                     tag="background_grid")

    def draw_cross(self, i: int, j: int):
        padding = self.case_size // 25
        upemtk.ligne(
            j * self.case_size + self.start_background + padding,
            i * self.case_size + self.start_background + padding,
            (j + 1) * self.case_size + self.start_background - padding,
            (i + 1) * self.case_size + self.start_background - padding,
            epaisseur=5,
            tag="cross",
            couleur="red"
        )
        upemtk.ligne(
            (j + 1) * self.case_size + self.start_background - padding,
            i * self.case_size + self.start_background + padding,
            j * self.case_size + self.start_background + padding,
            (i + 1) * self.case_size + self.start_background - padding,
            epaisseur=5,
            tag="cross",
            couleur="red"
        )

    def draw_circle(self, i: int, j: int):
        upemtk.cercle(
            j * self.case_size + self.start_background + self.case_size // 2,
            i * self.case_size + self.start_background + self.case_size // 2,
            self.case_size // 2 - self.case_size // 40,
            epaisseur=5,
            tag="circle",
            couleur="blue"
        )

    def get_index(self, x: int, y: int) -> tuple[int, int]:
        index_x = (x - self.start_background) // self.case_size
        index_y = (y - self.start_background) // self.case_size
        # x and y are reversed compared to a python matrix, so we revert it
        return index_y, index_x

    def text_winner(self, winner):
        upemtk.texte(self.start_background, self.end_background + self.start_background // 3,
                     f"The winner of the game is {winner} !", tag="winner_text", couleur="grey")

    def text_draw(self):
        upemtk.texte(self.start_background, self.end_background + self.start_background // 3,
                     f"The game ended in a draw.", tag="winner_text", couleur="grey")

    def text_turn(self, player: Motif):
        upemtk.efface("text_turn")
        color = "red" if player == Motif.CROSS else "blue"
        upemtk.texte(self.start_background, self.start_background // 2,
                     f"{player}, your turn to play !", tag="text_turn", couleur=color)


class Graphic(UI):
    def __init__(self, board: Board, *args, **kwargs):
        super().__init__(board)
        self.drawer = HandleDrawing(board.size, *args, **kwargs)

    def display(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                motif = self.board.board[i][j]
                if motif == Motif.CROSS:
                    self.drawer.draw_cross(i, j)
                elif motif == Motif.CIRCLE:
                    self.drawer.draw_circle(i, j)
        upemtk.mise_a_jour()

    def display_winner(self, winner: Motif):
        self.display()
        self.drawer.text_winner(winner)
        upemtk.mise_a_jour()
        upemtk.attend_ev()

    def display_draw(self):
        self.display()
        self.drawer.text_draw()
        upemtk.mise_a_jour()
        upemtk.attend_ev()

    def play(self, player: Motif):
        """Let the player pick his input and plays it."""
        self.drawer.text_turn(player)
        while True:
            x, y = upemtk.attend_clic_gauche()
            index_x, index_y = self.drawer.get_index(x, y)
            if 0 <= index_x < self.board.size and 0 <= index_y < self.board.size:
                try:
                    self.board.update(player, index_x, index_y)
                    return
                except AssertionError:
                    pass
