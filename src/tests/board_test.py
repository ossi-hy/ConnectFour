import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_empty_board_to_str(self):
        self.assertEqual(
            str(self.board), (Board.EMPTY_SYMBOL * self.board.w + "\n") * self.board.h
        )

    def test_empty_board_to_array(self):
        self.assertEqual(self.board.array(), [[0]*self.board.w]*self.board.h)

    def test_one_player_move(self):
        self.board.move(0)
        self.assertEqual(
            str(self.board), ".......\n.......\n.......\n.......\n.......\nO......\n"
        )

    def test_two_players_move_different_positions(self):
        self.board.move(0)
        self.board.move(6)
        self.assertEqual(
            str(self.board), ".......\n.......\n.......\n.......\n.......\nO.....X\n"
        )
    
    def test_two_players_move_same_position(self):
        self.board.move(0)
        self.board.move(0)
        self.assertEqual(
            str(self.board), ".......\n.......\n.......\n.......\nX......\nO......\n"
        )

    def test_game_ends_vertical_line(self):
        for _ in range(3):
            self.board.move(0)
            self.board.move(1)
        self.board.move(0)
        self.assertTrue(self.board.over)

    def test_game_ends_horizontal_line(self):
        for i in range(3):
            self.board.move(i)
            self.board.move(i)
        self.board.move(3)
        self.assertTrue(self.board.over)

