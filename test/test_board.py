import unittest
from lib.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_dividers(self):
        dividers = self.board.dividers()
        self.assertEqual(len(dividers), 7)
        for d in dividers[0:5]:
            self.assertEqual(d, '+---')
        self.assertEqual(dividers[6], '+---+')

    def test_full_divider(self):
        full_divider = self.board.full_divider()
        self.assertEqual(full_divider, '+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    unittest.main()
