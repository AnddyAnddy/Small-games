from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.ui_abstract import UI


class Terminal(UI):

    def display(self):
        print(self.board)

    def display_winner(self, winner: Motif):
        self.display()
        print(f"The winner of the game is {winner} !")

    def display_draw(self):
        self.display()
        print("The game ended in a draw.")

    def play(self, player: Motif):
        """Let the player pick his input and plays it."""

        print(f"{player}'s turn !")
        while True:
            try:
                row = int(input("Row: "))
                column = int(input("Column: "))
                self.board.update(player, row, column)
                return
            except (AssertionError, ValueError):
                print("You didn't write a valid combination for row and column")
