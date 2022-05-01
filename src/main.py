from board import Board
from solver import Solver
import argparse, logging, sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dim",
        type=int,
        nargs=2,
        default=[7, 6],
        metavar=("width", "height"),
        help="dimensions of the gameboard",
    )
    parser.add_argument(
        "-l",
        "--log",
        default="debug",
        choices=["none", "debug", "warning", "error"],
        help="logging level",
    )
    args = parser.parse_args()

    logging_levels = {
        "none": None,
        "debug": logging.DEBUG,
        "warning": logging.WARNING,
        "error": logging.ERROR,
    }
    level = logging_levels.get(args.log.lower())

    FORMAT = "%(module)s::%(funcName)s::%(lineno)d\t%(message)s"

    if level is None:
        pass
    else:
        logging.basicConfig(stream=sys.stderr, level=level, format=FORMAT)

    board = Board(args.dim[0], args.dim[1])

    solver = Solver(board.w)
    while True:
        print(f"Player {board.player} turn")
        try:
            col = int(input(f"Column [0-{board.w-1}] or exit [e]: "))
        except:
            break

        if col < 0 or col >= board.w:
            print("Invalid range")
            continue
        if board.can_move(col):
            board.move(col)
            print("Expected score: ", solver.eval_moves(board, depth=4))
        else:
            print("Can't move there")
        print(board)
        if board.is_over():
            print(f"Game over! Player {board.get_opponent()} won.")
            break


if __name__ == "__main__":
    main()
