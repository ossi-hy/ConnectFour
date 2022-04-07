import numpy as np
import logging


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

        self.movecount = 0
        self.over = False

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

    def array(self) -> list[list[int]]:
        ret_array = []
        for i in range(self.h - 1, -1, -1):
            row = []
            for j in range(self.w):
                a = 1 & self.state[0] >> (j * (self.h + 1) + i) == 1
                b = 1 & self.state[1] >> (j * (self.h + 1) + i) == 1
                if a:
                    row.append(1)
                elif b:
                    row.append(2)
                else:
                    row.append(0)
            ret_array.append(row)
        return ret_array

    def mask(self) -> int:
        """Calculates all occupied positions by both players

        Returns:
            int: bitboard with one in all occupied positions
        """
        return self.state[0] | self.state[1]

    def can_move(self, col: int) -> bool:
        height = (self.mask() >> (col * (self.h + 1)) & 0b111111).bit_length()
        return height < self.h

    def move(self, col: int) -> None:
        """Makes a move (drops a chip) on the board

        Args:
            col (int): column we want to drop our chip to

        Returns:
            bool: returns True if move was made
        """
        logging.debug(f"Mask: {self.mask()}")
        height = (self.mask() >> (col * (self.h + 1)) & 0b111111).bit_length()
        logging.debug(f"Height: {height}")

        pos = 1 << (col * (self.h + 1) + height)
        # Add move on the board of the player
        self.state[self.player] |= pos

        self.over = self.is_over()
        logging.debug(f"Over: {self.over}")
        
        # Change player
        self.player = 0 if self.player == 1 else 1

    def unmove(self, col: int) -> None:
        opponent = 0 if self.player == 1 else 1

        height = (self.mask() >> (col * (self.h + 1)) & 0b111111).bit_length() - 1
        pos = 1 << (col * (self.h + 1) + height)

        self.state[opponent] ^= pos


    def is_over(self) -> bool:
        """Checks if there is four in a row by current player

        Returns:
            bool: returns True if there is four in a row
        """

        # Horizontal check
        test = self.state[self.player] & (self.state[self.player] >> (self.h+1))
        if test & (test >> 2*(self.h+1)):
            return True
        
        # Vertical check
        test = self.state[self.player] & (self.state[self.player] >> 1)
        if test & (test >> 2):
            return True
        
        # Diagonal check
        test = self.state[self.player] & (self.state[self.player] >> self.h)
        if test & (test >> 2*self.h):
            return True
        
        # Diagonal check
        test = self.state[self.player] & (self.state[self.player] >> (self.h+2))
        if test & (test >> 2*(self.h+2)):
            return True    

        return False

