from board import Board
from transposition_table import TranspositionTable

class Solver:
    LARGE_NEGATIVE = -(1 << 31)
    LARGE_POSITIVE = 1 << 31

    def __init__(self, width: int) -> None:
        self.order = []
        for i in range(width):
            self.order.append(width // 2 + (1 - 2 * (i % 2)) * (i + 1) // 2)

        self.cache = TranspositionTable(256)

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
        highest_score = Solver.LARGE_NEGATIVE
        best_move = 0
        for x in range(board.w):
            if not board.can_move(x):
                scores.append(None)
                continue
            board.move(x)
            # Calculate opponent's score after player's move
            score = -self.negamax(
                board, Solver.LARGE_NEGATIVE, Solver.LARGE_POSITIVE, depth
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

        # Check if the game is over
        if board.is_over():
            return board.score()
        # Draw
        elif board.movecount == board.w * board.h:
            return 0

        alpha_orig = alpha
        # Search cache for this board
        key = board.key()
        if key in self.cache:
            value = self.cache[key]
            beta = min(beta, value)
            if alpha >= beta:
                return value

        value = -board.w * board.h
        for x in range(board.w):
            x = self.order[x]
            if not board.can_move(x):
                continue
            board.move(x)
            value = max(value, -self.negamax(board, -beta, -alpha, depth - 1))
            board.unmove(x)
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        if value <= alpha_orig:
            self.cache[key] = value

        return value
