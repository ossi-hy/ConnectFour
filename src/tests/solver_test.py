import unittest
import pytest  # type: ignore
from board import Board
from solver import Solver

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()
        self.solver = Solver(self.board.w)
    
    def test_find_winning_move_one_ahead(self):
        moves = [0,0,1,1,2,2]
        for move in moves:
            self.board.move(move)
        _, move, _ = self.solver.eval_moves(self.board, depth=1)
        self.assertEqual(move, 3)

    def test_find_defending_moves_four_ahead(self):
        moves = [3,3,4]
        for move in moves:
            self.board.move(move)
        scores, _, _ = self.solver.eval_moves(self.board, depth=4)
        best_of_bads = -self.board.w*self.board.h//2
        for x in range(self.board.w):
            if x == 2 or x == 5:
                continue
            best_of_bads = max(best_of_bads, scores[x])
        self.assertGreater(scores[5], best_of_bads)
        self.assertGreater(scores[2], best_of_bads)

    def test_first_column_full(self):
        for _ in range(self.board.h):
            self.board.move(0)
        scores, _, _ = self.solver.eval_moves(self.board, depth=1)
        self.assertIsNone(scores[0])
    
    def test_full_board(self):
        moves = "32162751756771355671355274632416432163244"
        for move in moves:
            self.board.move(int(move) - 1)
        _, _, score = self.solver.eval_moves(self.board, depth=13)
        self.assertEqual(score, 0)

    @pytest.mark.slow
    def test_positions_from_file(self):
        filename = "src/tests/test_depth_13.txt"
        lines = []
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            # Create empty board for each new sequence
            board = Board()
            # Each line will consist of sequence of moves and expected score for the first player 
            moves, expected_score = tuple(line.strip().split(' '))
            expected_score = int(expected_score)
            for move in moves:
                board.move(int(move) - 1)
            score = self.solver.solve(board, depth=14)
            self.assertEqual(score, expected_score)
