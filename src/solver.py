from board import Board
import numpy as np
import logging

class Solver:
    def __init__(self) -> None:
        pass

    def negamax(self, board: Board, alpha: int, beta: int):
        assert(alpha < beta)
        