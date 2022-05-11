from board import Board
from transposition_table import TranspositionTable
from copy import copy, deepcopy

class Solver:
    def __init__(self, width: int) -> None:
        self.order = []
        for i in range(width):
            self.order.append(width // 2 + (1 - 2 * (i % 2)) * (i + 1) // 2)

        # Upper bound cache
        self.ub_cache = TranspositionTable(2**24)
        # Lower bound cache
        self.lb_cache = TranspositionTable(2**24)

    def eval_moves(self, board: Board, depth: int) -> tuple[list[int], int, int]:
        """Evaluates all the possible moves from given position for current player.

        Args:
            board (Board): Board to be evaluated
            depth (int): Search depth for negamax algorithm

        Returns:
            tuple[list[int], int, int]: Returns list of expected scores for each position (None if move is not possible),
            column of the best move and expected score for the best move
        """
        scores = []
        highest_score = -board.w*board.h//2
        best_move = 0
        for x in range(board.w):
            if not board.can_move(x):
                scores.append(None)
                continue
            board.move(x)
            # Calculate opponent's score after player's move
            score = -self.negamax(
                board, -board.w*board.h//2, board.w*board.h//2, depth
            )
            board.unmove(x)

            if score > highest_score:
                best_move = x
                highest_score = score

            scores.append(score)

        return scores, best_move, highest_score

    def negamax(self, board: Board, alpha: int, beta: int, depth: int) -> int:
        """Variation of minimax algorithm for symmetric games.
        Finds best move by expanding all possible moves recursively until draw or other player wins.
        Alpha-beta pruning is used to reduce the search space by cutting branches that won't affect final choice.

        Args:
            board (Board): Board to be evaluated
            alpha (int): Alpha
            beta (int): Beta
            depth (int): Depth of the search (One turn = 2 moves = 2 depth)

        Returns:
            int: Evaluation of the given position
        """
        if depth == 0:
            return 0

        if board.movecount == board.w * board.h:
            if board.is_over():
                return board.score()
            return 0

        # Check if the game is over
        if board.is_over():
            return board.score()

        
        alpha_orig = alpha
        # Search cache for this board
        key = board.key()
        if key in self.ub_cache:
            value = self.ub_cache[key]
            beta = min(beta, value)
            if alpha >= beta:
                return value
        elif key in self.lb_cache:
            value = self.lb_cache[key]
            alpha = max(alpha, value)          
            if alpha >= beta:
                return value
        

        max_val = (board.w * board.h + 1 - board.movecount) // 2
        if beta > max_val:
            beta = max_val
            if alpha >= beta:
               return beta


        for x in self.order:
            if board.can_move(x):
                board.move(x)
                value = -self.negamax(board, -beta, -alpha, depth - 1)
                board.unmove(x)

                if value >= beta:
                    self.lb_cache[key] = value
                    return value

                if value > alpha:
                    alpha = value

        if alpha <= alpha_orig:
            self.ub_cache[key] = alpha


        return alpha
