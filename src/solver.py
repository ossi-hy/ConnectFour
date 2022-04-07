from board import Board
import numpy as np
import logging

class Solver:
    def __init__(self) -> None:
        pass

    def negamax(self, board: Board, alpha: int, beta: int):
        assert(alpha < beta)

        ## Check if the game is over
        if board.is_over():
            return board.score()

        # Check for draw
        if board.movecount == board.w * board.h:
            return 0

        value = - board.w * board.h
        for x in range(board.w):
            if not board.can_move(x):
                continue
            board.move(x)
            value = max(value, -self.negamax(board, -beta, -alpha))
            board.unmove(x)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        
        return value
