from board import Board

import numpy as np

def main() -> None:
    board = Board()
    print(board)

    board.move(1)
    print(board)

    board.move(1)
    print(board)

if __name__ == "__main__":
    main()