import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_empty_board_to_str(self):
        self.assertEqual(
            str(self.board), ".......\n.......\n.......\n.......\n.......\n.......\n"
        )
