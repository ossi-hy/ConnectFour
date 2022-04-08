import unittest
from board import Board
from solver import Solver

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()
        self.solver = Solver()
    
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
        self.assertEqual(scores[5], 0)
        self.assertEqual(scores[2], 0)
        for x in range(self.board.w):
            if x == 2 or x == 5:
                continue
            self.assertLess(scores[x], 0)