import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_empty_board_to_str(self):
        self.assertEqual(
            str(self.board), (Board.EMPTY_SYMBOL*self.board.w+'\n')*self.board.h
        )

    def test_one_player_move(self):
        self.board.move(0)
        self.assertEqual(str(self.board), ".......\n.......\n.......\n.......\n.......\nO......\n")