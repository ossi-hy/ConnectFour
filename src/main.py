from board import Board
from solver import Solver
import argparse


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
        "-D",
        "--depth",
        type=int,
        default=8,
        help="depth of the search algorithm",
    )
    args = parser.parse_args()

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
            print("Expected score: ", solver.eval_moves(board, depth=args.depth))
        else:
            print("Can't move there")
        print(board)
        if board.is_over():
            print(f"Game over! Player {board.get_opponent()} won.")
            break


if __name__ == "__main__":
    main()
