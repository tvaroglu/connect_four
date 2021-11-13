import unittest
from lib.board import Board
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(self.board.construct_board())
        self.first_row = self.game.board[self.game.game_rows[0]]
        self.second_row = self.game.board[self.game.game_rows[1]]
        self.empty_row = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   |']
        self.empty_column = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   |']

    def test_game_rows(self):
        for index in self.game.game_rows:
            self.assertEqual(self.game.board[index], self.empty_row)
            self.assertEqual(len(self.game.board[index]), 7)
        self.assertEqual(self.game.join_row(self.empty_row), ''.join(self.empty_row))

    def test_piece_placed(self):
        self.assertEqual(self.game.piece_placed(), 'Nice move!')

    def test_place_valid_piece(self):
        self.assertEqual(self.first_row[0], '|   ')
        self.assertEqual(self.game.place_piece('R', 1), self.game.piece_placed())
        self.assertEqual(self.first_row[0], '| R ')
        self.game.place_piece('R', 1)
        self.assertEqual(self.second_row[0], '| R ')
        self.assertEqual(self.first_row[6], '|   |')
        self.game.place_piece('B', 7)
        self.assertEqual(self.first_row[6], '| B |')
        self.game.place_piece('B', 7)
        self.assertEqual(self.second_row[6], '| B |')

    def test_place_invalid_color(self):
        self.assertEqual(self.game.invalid_color(), 'Sorry! Invalid color, please try again.')
        self.assertEqual(self.game.place_piece('G', 1), self.game.invalid_color())

    def test_place_invalid_piece(self):
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 7)
        self.game.place_piece('R', 7)
        self.game.place_piece('B', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.assertEqual(self.game.invalid_placement(), "Sorry! Can't place a piece there, please try another move.")
        self.assertEqual(self.game.place_piece('B', 1), self.game.invalid_placement())

    def test_evaluate_rows_black_wins(self):
        self.game.place_piece('B', 1)
        self.game.place_piece('B', 2)
        self.game.place_piece('B', 3)
        self.assertEqual(self.game.evaluate_rows(), '')
        self.game.place_piece('R', 5)
        self.game.place_piece('B', 4)
        self.assertEqual(self.game.evaluate_rows(), 'Black')

    def test_evaluate_rows_red_wins(self):
        self.game.place_piece('R', 7)
        self.game.place_piece('R', 6)
        self.game.place_piece('R', 5)
        self.assertEqual(self.game.evaluate_rows(), '')
        self.game.place_piece('B', 3)
        self.game.place_piece('R', 4)
        self.assertEqual(self.game.evaluate_rows(), 'Red')

    def test_evaluate_columns_black_wins(self):
        self.game.place_piece('B', 6)
        self.game.place_piece('R', 6)
        self.game.place_piece('B', 7)
        self.game.place_piece('B', 7)
        self.game.place_piece('B', 7)
        aggregated = self.game.aggregate_columns()
        self.assertEqual(self.game.evaluate_columns(aggregated), '')
        for column in aggregated[0:-2]:
            self.assertEqual(column, self.empty_column)
        self.assertEqual(aggregated[-2], ['|   ', '|   ', '|   ', '|   ', '| R ', '| B |'])
        self.assertEqual(aggregated[-1], ['|   ', '|   ', '|   ', '| B ', '| B ', '| B |'])
        self.game.place_piece('B', 7)
        self.assertEqual(self.game.evaluate_rows(), '')
        self.assertEqual(self.game.evaluate_columns(self.game.aggregate_columns()), 'Black')

    def test_evaluate_columns_red_wins(self):
        self.game.place_piece('R', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('R', 1)
        self.assertEqual(self.game.evaluate_columns(self.game.aggregate_columns()), '')
        self.game.place_piece('B', 7)
        self.game.place_piece('R', 1)
        self.assertEqual(self.game.evaluate_columns(self.game.aggregate_columns()), 'Red')

    def test_evaluate_diagonals(self):
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.game.place_piece('B', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 2)
        self.game.place_piece('R', 2)
        self.game.place_piece('B', 7)
        self.game.place_piece('R', 6)
        self.game.place_piece('R', 6)
        print("\n")
        self.game.render_board()


if __name__ == '__main__':
    unittest.main()
