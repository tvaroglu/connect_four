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

    def test_empty_row(self):
        empty_row = self.board.empty_row()
        self.assertEqual(len(empty_row), 7)
        for cell in empty_row[0:5]:
            self.assertEqual(cell, '|   ')
        self.assertEqual(empty_row[6], '|   |')

    def test_join_row(self):
        empty_row = self.board.empty_row()
        self.assertEqual(self.board.join_row(empty_row), '|   |   |   |   |   |   |   |')

    def test_construct_board(self):
        board = self.board.construct_board()
        labels = self.board.full_column_label()
        divider = self.board.row_dividers()
        empty_row = self.board.empty_row()
        self.assertEqual(len(board), 14)
        self.assertEqual(board[0], labels)
        for index, row in enumerate(board[1:-1]):
            self.assertEqual(len(row), 7)
            if index % 2 == 0:
                self.assertEqual(row, divider)
            else:
                self.assertEqual(row, empty_row)

    def test_print_board_setup(self):
        board = self.board.construct_board(printable=True)
        labels = self.board.full_column_label()
        divider = self.board.full_row_divider()
        empty_row = self.board.join_row(self.board.empty_row())
        self.assertEqual(board[0], labels)
        for index, row in enumerate(board[1:-1]):
            if index % 2 == 0:
                self.assertEqual(row, divider)
            else:
                self.assertEqual(row, empty_row)
        # print("\n")
        # self.board.print_board()


if __name__ == '__main__':
    unittest.main()
