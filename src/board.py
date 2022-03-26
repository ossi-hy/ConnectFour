from tkinter import W
import numpy as np


class Board:
    def __init__(self, width: int = 7, height: int = 6) -> None:
        self.w = width
        self.h = height

        # Represent state with bitboards, one for each player
        self.state = (0, 0)
        # 0 = Player A, 1 = Player B
        self.player = 0

    def __str__(self):
        ret_string = ""
        for i in range(self.h - 1, -1, -1):
            for j in range(self.w):
                a = 1 & self.state[0] >> (j * (self.w + 1) + i) == 1
                b = 1 & self.state[1] >> (j * (self.w + 1) + i) == 1
                if a:
                    ret_string += "O"
                elif b:
                    ret_string += "X"
                else:
                    ret_string += "."
            ret_string += "\n"
        return ret_string

    def mask(self):
        return self.state[0] | self.state[1]

    def legal_move(self, col):
        pass

    def move(self, col):
        self.state[self.player] |= 1

    
