import sys

from src.tictactoe.game_mechanic.game import Game
from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.ui_all_combination import AllMoves
from src.tictactoe.user_interface.ui_debug import Debug
from src.tictactoe.user_interface.ui_terminal import Terminal


def terminal():
    Game(Terminal).main_loop()


def debug():
    for i in range(len(Debug.DEBUG_MOVES)):
        Game(Debug, test_index=i).main_loop()


def stats():
    winner_count = {Motif.CROSS: 0, Motif.CIRCLE: 0, Motif.BLANK: 0}
    for i in range(len(AllMoves.ALL_MOVES) // 5):
        game = Game(AllMoves, test_index=i)
        winner = game.main_loop()
        winner_count[winner] += 1
    print("WINNER COUNT")
    print("\n".join([f"{winner}: {count}" for winner, count in winner_count.items()]))


if __name__ == '__main__':
    mode = sys.argv[1:]
    if not mode:
        print("No mode were selected, use command line arguments with 'terminal', 'debug' or 'stats' to select a mode.")
        print("Terminal mode is selected by default.")
        terminal()
    selected_mode = mode[0].strip().lower()
    print(f"{selected_mode=}")

    match selected_mode:
        case "terminal":
            terminal()
        case "debug":
            debug()
        case "stats":
            stats()
        case _:
            print("You didn't seize a valid mode, it must be: terminal, debug or stats")
