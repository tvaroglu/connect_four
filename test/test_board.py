import unittest
from lib.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_column_labels(self):
        labels = self.board.column_labels()
        self.assertEqual(len(labels), 7)
        counter = 1
        for l in labels:
            self.assertEqual(l, f' {str(counter)}  ')
            counter += 1

    def test_full_column_label(self):
        full_label = self.board.full_column_label()
        self.assertEqual(full_label, '  1   2   3   4   5   6   7  ')

    def test_row_dividers(self):
        dividers = self.board.row_dividers()
        self.assertEqual(len(dividers), 7)
        for d in dividers[0:5]:
            self.assertEqual(d, '+---')
        self.assertEqual(dividers[6], '+---+')

    def test_full_row_divider(self):
        full_row_divider = self.board.full_row_divider()
        self.assertEqual(full_row_divider, '+---+---+---+---+---+---+---+')

    def test_board_setup(self):
        board = self.board.board_setup()
        labels = self.board.full_column_label()
        self.assertEqual(board[0], labels)
        for row in board[1:-1]:
            self.assertEqual(row, self.board.full_row_divider())


if __name__ == '__main__':
    unittest.main()
