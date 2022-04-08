from board import Board
import numpy as np
import logging

class Solver:
    LARGE_NEGATIVE = -(1<<31)
    LARGE_POSITIVE = 1<<31

    def __init__(self) -> None:
        pass

    def eval_moves(self, board: Board, depth: int) -> int:
        scores = []
        highest_score = Solver.LARGE_NEGATIVE
        best_move = 0
        for x in range(board.w):
            if not board.can_move(x):
                scores.append(None)
                continue
            board.move(x)
            # Calculate opponent's score after player's move
            score = -self.negamax(board, Solver.LARGE_NEGATIVE, Solver.LARGE_POSITIVE, depth)
            board.unmove(x)
            if score > highest_score:
                best_move = x
                highest_score = score
            scores.append(score)
        return scores, best_move, highest_score

    def negamax(self, board: Board, alpha: int, beta: int, depth: int) -> int:
        assert(alpha < beta)
        if depth == 0:
            return 0
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
            value = max(value, -self.negamax(board, -beta, -alpha, depth-1))
            board.unmove(x)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        
        return value
