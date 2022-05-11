from __future__ import annotations
from functools import reduce
from copy import copy

class Board:
    EMPTY_SYMBOL = ". "
    PLAYER_A_SYMBOL = "O "
    PLAYER_B_SYMBOL = "X "

    def __init__(self, width: int = 7, height: int = 6) -> None:
        """Constructor for Board

        Args:
            width (int, optional): Width of the playable board. Defaults to 7.
            height (int, optional): Height of the playable board. Defaults to 6.
        """
        self.w: int = width
        self.h: int = height

        # Represent state with bitboards, one for each player
        self.state: list[int] = [0, 0]
        # 0 = Player A, 1 = Player B
        self.player: int = 0

        self.movecount: int = 0

        self.col_heights = [0] * self.w

    def __str__(self) -> str:
        """Converts Board to human readable string

        Returns:
            str: gameboard as multiline string
        """
        ret_string = ""
        for i in range(self.h - 1, -1, -1):
            for j in range(self.w):
                a = 1 & self.state[0] >> (j * (self.h + 1) + i) == 1
                b = 1 & self.state[1] >> (j * (self.h + 1) + i) == 1
                if a:
                    ret_string += Board.PLAYER_A_SYMBOL
                elif b:
                    ret_string += Board.PLAYER_B_SYMBOL
                else:
                    ret_string += Board.EMPTY_SYMBOL
            ret_string += "\n"
        return ret_string

    def key(self) -> int:
        return (self.state[0] | self.state[1]) + self.state[self.player]

    def can_move(self, col: int) -> bool:
        """Checks if you can make a move to the given colum (if there's space left)

        Args:
            col (int): Column we would like to drop chip to

        Returns:
            bool: True if the move is possible
        """
        return self.col_heights[col] < self.h

    def move(self, col: int) -> None:
        """Makes a move (drops a chip) on the board

        Args:
            col (int): column we want to drop our chip to

        Returns:
            bool: returns True if move was made
        """
        # Add move on the board of the player
        self.state[self.player] |= 1 << col * (self.h + 1) + self.col_heights[col]

        self.col_heights[col] += 1

        self.movecount += 1

        # Change player
        self.player ^= 1

    def unmove(self, col: int) -> None:
        """Backtrack the move made to the given column

        Args:
            col (int): column to remove the last played chip from
        """
        self.player ^= 1

        self.col_heights[col] -= 1

        self.state[self.player] ^= 1 << col * (self.h + 1) + self.col_heights[col]

        self.movecount -= 1

    def is_over(self) -> bool:
        """Checks if there is four in a row by previous player

        Returns:
            bool: returns True if there is four in a row
        """

        opp = self.player ^ 1

        state = self.state[opp]

        # Horizontal check
        test = state & state >> self.h + 1
        if test & test >> 2 * (self.h + 1):
            return True

        # Vertical check
        test = state & state >> 1
        if test & test >> 2:
            return True

        # Diagonal check
        test = state & state >> self.h
        if test & test >> 2 * self.h:
            return True

        # Diagonal check
        test = state & state >> self.h + 2
        if test & test >> 2 * (self.h + 2):
            return True

        return False

    def score(self) -> int:
        """Returns the score for the current player.
        This should be only used after the game is over.

        Returns:
            int: score of the current player
        """
        return -(self.w * self.h + 1 - self.movecount) // 2
