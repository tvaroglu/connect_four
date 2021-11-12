import unittest
from lib.board import Board
from lib.turn import Turn

class TestTurn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.turn = Turn(self.board.construct_board())
        self.first_row = self.turn.board[self.turn.game_rows[0]]
        self.second_row = self.turn.board[self.turn.game_rows[1]]
        self.empty_row = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   |']
        self.empty_column = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   |']

    def test_game_rows(self):
        for index in self.turn.game_rows:
            self.assertEqual(self.turn.board[index], self.empty_row)
            self.assertEqual(len(self.turn.board[index]), 7)
        self.assertEqual(self.turn.join_row(self.empty_row), ''.join(self.empty_row))

    def test_piece_placed(self):
        self.assertEqual(self.turn.piece_placed(), 'Nice move!')

    def test_place_valid_piece(self):
        self.assertEqual(self.first_row[0], '|   ')
        self.assertEqual(self.turn.place_piece('R', 1), self.turn.piece_placed())
        self.assertEqual(self.first_row[0], '| R ')
        self.turn.place_piece('R', 1)
        self.assertEqual(self.second_row[0], '| R ')
        self.assertEqual(self.first_row[6], '|   |')
        self.turn.place_piece('B', 7)
        self.assertEqual(self.first_row[6], '| B |')
        self.turn.place_piece('B', 7)
        self.assertEqual(self.second_row[6], '| B |')

    def test_place_invalid_color(self):
        self.assertEqual(self.turn.invalid_color(), 'Sorry! Invalid color, please try again.')
        self.assertEqual(self.turn.place_piece('G', 1), self.turn.invalid_color())

    def test_place_invalid_piece(self):
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 1)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 7)
        self.turn.place_piece('R', 7)
        self.turn.place_piece('B', 1)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('B', 1)
        self.assertEqual(self.turn.invalid_placement(), "Sorry! Can't place a piece there, please try another move.")
        self.assertEqual(self.turn.place_piece('B', 1), self.turn.invalid_placement())

    def test_evaluate_rows_black_wins(self):
        self.turn.place_piece('B', 1)
        self.turn.place_piece('B', 2)
        self.turn.place_piece('B', 3)
        self.assertEqual(self.turn.evaluate_rows(), '')
        self.turn.place_piece('R', 5)
        self.turn.place_piece('B', 4)
        self.assertEqual(self.turn.evaluate_rows(), 'Black')

    def test_evaluate_rows_red_wins(self):
        self.turn.place_piece('R', 7)
        self.turn.place_piece('R', 6)
        self.turn.place_piece('R', 5)
        self.assertEqual(self.turn.evaluate_rows(), '')
        self.turn.place_piece('B', 3)
        self.turn.place_piece('R', 4)
        self.assertEqual(self.turn.evaluate_rows(), 'Red')

    def test_evaluate_columns_black_wins(self):
        self.turn.place_piece('B', 6)
        self.turn.place_piece('R', 6)
        self.turn.place_piece('B', 7)
        self.turn.place_piece('B', 7)
        self.turn.place_piece('B', 7)
        aggregated = self.turn.aggregate_columns()
        self.assertEqual(self.turn.evaluate_columns(aggregated), '')
        for column in aggregated[0:-2]:
            self.assertEqual(column, self.empty_column)
        self.assertEqual(aggregated[-2], ['|   ', '|   ', '|   ', '|   ', '| R ', '| B |'])
        self.assertEqual(aggregated[-1], ['|   ', '|   ', '|   ', '| B ', '| B ', '| B |'])
        self.turn.place_piece('B', 7)
        self.assertEqual(self.turn.evaluate_rows(), '')
        self.assertEqual(self.turn.evaluate_columns(self.turn.aggregate_columns()), 'Black')

    def test_evaluate_columns_red_wins(self):
        self.turn.place_piece('R', 1)
        self.turn.place_piece('R', 1)
        self.turn.place_piece('R', 1)
        self.assertEqual(self.turn.evaluate_columns(self.turn.aggregate_columns()), '')
        self.turn.place_piece('B', 7)
        self.turn.place_piece('R', 1)
        # print("\n")
        # self.turn.render_board()
        self.assertEqual(self.turn.evaluate_columns(self.turn.aggregate_columns()), 'Red')


if __name__ == '__main__':
    unittest.main()
