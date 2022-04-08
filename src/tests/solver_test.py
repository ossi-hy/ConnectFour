import unittest
from board import Board
from solver import Solver

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()
        self.solver = Solver()
    
    def test_find_winning_one_move_ahead(self):
        moves = [0,0,1,1,2,2]
        for move in moves:
            self.board.move(move)
        _, move, _ = self.solver.eval_moves(self.board, depth=1)
        self.assertEqual(move, 3)