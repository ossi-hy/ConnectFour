from __future__ import annotations
from board import Board
from solver import Solver
import argparse
from time import time


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
        default=9,
        help="depth of the search algorithm",
    )
    parser.add_argument(
        "-a", "--against", action="store_true", help="play against computer"
    )
    parser.add_argument(
        "-p", "--profile", action="store_true", help="profile code by running slow test"
    )
    args = parser.parse_args()

    board = Board(args.dim[0], args.dim[1])

    solver = Solver(board.w)

    if args.profile:
        filename = "src/tests/test_depth_mid_13.txt"
        lines = []
        with open(filename, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            # Create empty board for each new sequence
            board = Board()
            # Each line will consist of sequence of moves and expected score for the first player
            moves, expected_score = tuple(line.strip().split(" "))
            expected_score = int(expected_score)
            for move in moves:
                board.move(int(move) - 1)
            score = solver.solve(board, depth=15)
            if score != expected_score:
                print("TEST FAILED")
                return
        print(f"Evaluated nodes: {solver.count}")
        return

    total_time = 0

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
            start = time()
            scores, move, _ = solver.eval_moves(board, depth=args.depth)
            end = time()
            total_time = end - start
            if args.against:
                board.move(move)
            else:
                print("Expected scores for each position: ", scores)
                print("Best move: ", move)
        else:
            print("Can't move there")
        print(board)
        if total_time > 0:
            print(
                f"Evaluated: {solver.count} nodes in {total_time:.2f}s ({int(solver.count/total_time)}n/s)"
            )
        solver.count = 0
        if board.is_over():
            print(f"Game over! Player {board.get_opponent()} won.")
            break
        elif board.movecount == board.w * board.h:
            print("Draw!")
            break


if __name__ == "__main__":
    main()
