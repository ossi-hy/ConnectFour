import unittest
from transposition_table import TranspositionTable

class TranspositionTableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.table = TranspositionTable(4)

    def test_overflow(self):
        self.table[1] = 1
        self.table[2] = 2
        self.table[3] = 3
        self.table[4] = 4
        self.assertEqual(len(self.table), 4)
        self.table[5] = 5
        self.assertEqual(len(self.table), 4)
        self.table[5] = 6
        self.assertEqual(len(self.table), 4)

