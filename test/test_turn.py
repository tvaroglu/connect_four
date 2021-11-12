import unittest
from lib.board import Board
from lib.turn import Turn

class TestTurn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.full_board = self.board.construct_board()
        self.turn = Turn(self.full_board)
        self.first_row = self.turn.board[self.turn.game_rows[0]]
        self.second_row = self.turn.board[self.turn.game_rows[1]]
        self.empty_row = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   |']

    def test_game_rows(self):
        for index in self.turn.game_rows:
            self.assertEqual(self.turn.board[index], self.empty_row)
            self.assertEqual(len(self.turn.board[index]), 7)
        self.assertEqual(self.turn.join_row(self.empty_row), ''.join(self.empty_row))

    def test_place_valid_piece(self):
        self.assertEqual(self.first_row[0], '|   ')
        self.turn.place_piece('R', 1)
        self.assertEqual(self.first_row[0], '| R ')

        self.assertEqual(self.first_row[6], '|   |')
        self.turn.place_piece('B', 7)
        self.assertEqual(self.first_row[6], '| B |')

        self.turn.place_piece('B', 1)
        self.assertEqual(self.first_row[0], '| R ')
        self.assertEqual(self.second_row[0], '| B ')

    def test_place_invalid_piece(self):
        self.turn.place_piece('B', 7)
        self.turn.place_piece('B', 7)
        self.turn.place_piece('B', 7)
        self.turn.place_piece('B', 6)
        self.turn.place_piece('R', 5)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 1)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 1)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 1)
        # print("\n")
        # self.turn.render_board()
        # self.turn.place_piece('B', 1)
        self.assertEqual(self.turn.invalid_placement(), "Sorry! Can't place a piece there, please try another move.")


if __name__ == '__main__':
    unittest.main()
