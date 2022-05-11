import unittest
from board import Board


def column_equals(board: Board, col: int, column_str: str):
    board_str = str(board)
    for y in range(board.h):
        if board_str[y * (board.w + 1) + col] != column_str[y]:
            return False
    return True


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_empty_board_to_str(self):
        self.assertEqual(
            str(self.board), (Board.EMPTY_SYMBOL * self.board.w + "\n") * self.board.h
        )

    def test_one_player_move(self):
        self.board.move(0)
        self.assertEqual(
            str(self.board),
            (Board.EMPTY_SYMBOL * self.board.w + "\n") * (self.board.h - 1)
            + self.board.PLAYER_A_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 1) + "\n"),
        )
        self.assertEqual(self.board.movecount, 1)

    def test_two_players_move_different_positions(self):
        self.board.move(0)
        self.board.move(6)
        self.assertEqual(
            str(self.board),
            (Board.EMPTY_SYMBOL * self.board.w + "\n") * (self.board.h - 1)
            + self.board.PLAYER_A_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 2) + Board.PLAYER_B_SYMBOL + "\n"),
        )
        self.assertEqual(self.board.movecount, 2)

    def test_two_players_move_same_position(self):
        self.board.move(0)
        self.board.move(0)
        self.assertEqual(
            str(self.board), (Board.EMPTY_SYMBOL * self.board.w + "\n") * (self.board.h - 2)
            + self.board.PLAYER_B_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 1) + "\n")
            + self.board.PLAYER_A_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 1) + "\n"),
        )

    def test_two_players_fill_first_column(self):
        for _ in range(self.board.h + 1):
            if self.board.can_move(0):
                self.board.move(0)
        self.assertEqual(
            str(self.board), (self.board.PLAYER_B_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 1) + "\n")
            + self.board.PLAYER_A_SYMBOL
            + (Board.EMPTY_SYMBOL * (self.board.w - 1) + "\n"))*(self.board.h//2),
        )

    def test_game_ends_vertical_line(self):
        for _ in range(3):
            self.board.move(0)
            self.board.move(1)
        self.assertFalse(self.board.is_over())
        self.board.move(0)
        self.assertTrue(self.board.is_over())

    def test_game_ends_horizontal_line(self):
        for i in range(3):
            self.board.move(i)
            self.board.move(i)
        self.assertFalse(self.board.is_over())
        self.board.move(3)
        self.assertTrue(self.board.is_over())

    def test_game_ends_diagonal1_line(self):
        moves = [0, 1, 1, 2, 3, 2, 2, 3, 4, 3]
        for move in moves:
            self.board.move(move)
        self.assertFalse(self.board.is_over())
        self.board.move(3)
        self.assertTrue(self.board.is_over())

    def test_game_ends_diagonal2_line(self):
        moves = [0, 1, 1, 2, 3, 2, 2, 3, 4, 3]
        for move in moves:
            self.board.move(6 - move)
        self.assertFalse(self.board.is_over())
        self.board.move(6 - 3)
        self.assertTrue(self.board.is_over())

    def test_unmove_one(self):
        for x in range(self.board.w):
            self.board.move(x)
            self.board.unmove(x)
            self.assertEqual(
                str(self.board),
                (Board.EMPTY_SYMBOL * self.board.w + "\n") * self.board.h,
            )

    def test_unmove_two(self):
        for x1 in range(self.board.w):
            for x2 in range(self.board.w):
                print(x1, x2)
                self.board.move(x1)
                self.board.move(x2)
                self.board.unmove(x2)
                self.board.unmove(x1)
                self.assertEqual(
                    str(self.board),
                    (Board.EMPTY_SYMBOL * self.board.w + "\n") * self.board.h,
                )
