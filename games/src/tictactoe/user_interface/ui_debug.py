from src.tictactoe.game_mechanic.board import Board
from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.ui_abstract import UI

data_end_game = [
    {
        Motif.CROSS: [(0, 0), (1, 1), (2, 2)],
        Motif.CIRCLE: [(0, 1), (1, 0)],
        "winner": Motif.CROSS,
        "description": f"diagonal top left bottom right {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(2, 0), (1, 1), (0, 2)],
        Motif.CIRCLE: [(0, 0), (1, 0)],
        "winner": Motif.CROSS,
        "description": f"diagonal top right bottom left {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(0, 1), (1, 0), (2, 1)],
        Motif.CIRCLE: [(0, 0), (1, 1), (2, 2)],
        "winner": Motif.CIRCLE,
        "description": f"diagonal top left bottom right {Motif.CIRCLE} wins"
    },
    {
        Motif.CROSS: [(0, 0), (1, 0), (1, 2)],
        Motif.CIRCLE: [(2, 0), (1, 1), (0, 2)],
        "winner": Motif.CIRCLE,
        "description": f"diagonal top right bottom left {Motif.CIRCLE} wins"
    },
    {
        Motif.CROSS: [(0, 0), (0, 1), (0, 2)],
        Motif.CIRCLE: [(1, 0), (1, 1)],
        "winner": Motif.CROSS,
        "description": f"top row {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(1, 0), (1, 1), (1, 2)],
        Motif.CIRCLE: [(0, 0), (0, 1)],
        "winner": Motif.CROSS,
        "description": f"middle row {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(2, 0), (2, 1), (2, 2)],
        Motif.CIRCLE: [(0, 0), (0, 1)],
        "winner": Motif.CROSS,
        "description": f"bottom row {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(0, 0), (1, 0), (2, 0)],
        Motif.CIRCLE: [(0, 1), (0, 2)],
        "winner": Motif.CROSS,
        "description": f"left column {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(0, 1), (1, 1), (2, 1)],
        Motif.CIRCLE: [(2, 2), (0, 2)],
        "winner": Motif.CROSS,
        "description": f"middle column {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(0, 2), (1, 2), (2, 2)],
        Motif.CIRCLE: [(0, 0), (0, 1)],
        "winner": Motif.CROSS,
        "description": f"right column {Motif.CROSS} wins"
    },
    {
        Motif.CROSS: [(0, 0), (0, 1), (1, 2), (2, 0), (2, 2)],
        Motif.CIRCLE: [(0, 2), (1, 0), (1, 1), (2, 1)],
        "winner": Motif.BLANK,
        "description": f"draw"
    }
]


class Debug(UI):
    DEBUG_MOVES = data_end_game

    def __init__(self, board: Board, test_index=0):
        super().__init__(board)
        self.test_index = test_index
        self.turn = 0

    def display(self):
        pass

    def display_winner(self, winner: Motif):
        print(self.DEBUG_MOVES[self.test_index]["description"])
        print(self.board)
        print(f"Predicted winner: {self.DEBUG_MOVES[self.test_index]['winner']}, actual winner: {winner}")
        assert winner == self.DEBUG_MOVES[self.test_index]["winner"]

    def display_draw(self):
        print(self.DEBUG_MOVES[self.test_index]["description"])
        print(self.board)
        print(f"Predicted winner: {self.DEBUG_MOVES[self.test_index]['winner']}, actual winner: {Motif.BLANK}")
        assert Motif.BLANK == self.DEBUG_MOVES[self.test_index]["winner"]

    def play(self, player: Motif):
        """Select and play the next move to do corresponding to the player."""
        row, column = self.DEBUG_MOVES[self.test_index][player][self.board.motif_count // 2]
        self.board.update(player, row, column)
