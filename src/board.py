from tkinter import W
import numpy as np


class Board:
    EMPTY_SYMBOL = "."
    PLAYER_A_SYMBOL = "O"
    PLAYER_B_SYMBOL = "X"

    def __init__(self, width: int = 7, height: int = 6) -> None:
        self.w = width
        self.h = height

        # Represent state with bitboards, one for each player
        self.state = [0, 0]
        # 0 = Player A, 1 = Player B
        self.player = 0

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

    def mask(self):
        """Calculates all occupied positions by both players

        Returns:
            int: bitboard with one in all occupied positions
        """
        return self.state[0] | self.state[1]

    def move(self, col: int):
        height = (self.mask() >> (col * (self.h + 1)) & 111111).bit_length()
        if height >= self.h:
            return False

        self.state[self.player] |= 1 << (col * (self.h + 1) + height)
        self.player = ~self.player

        return True
