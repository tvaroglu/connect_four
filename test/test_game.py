import unittest
from lib.board import Board
from lib.player import Player
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player_1 = Player('John', 'R')
        self.player_2 = Player('Jane', 'B')
        self.game = Game(self.board.construct_board(), self.player_1, self.player_2)
        self.first_row = self.game.board[self.game.game_rows[0]]
        self.second_row = self.game.board[self.game.game_rows[1]]
        self.empty_row = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   |']
        self.empty_column = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   |']

    def test_join_row(self):
        self.assertEqual(self.game.join_row(self.empty_row), '|   |   |   |   |   |   |   |')

    def test_game_rows(self):
        for index in self.game.game_rows:
            self.assertEqual(self.game.board[index], self.empty_row)
            self.assertEqual(len(self.game.board[index]), 7)

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

    def test_reformat_last_cell(self):
        formatted = self.game.format_cell('R')
        self.assertEqual(formatted, '| R ')
        self.assertEqual(self.game.reformat_last_cell(formatted), '| R |')

    def test_place_invalid_color(self):
        self.assertEqual(self.game.invalid_color(), 'Sorry! Invalid color, please try again.')
        self.assertEqual(self.game.place_piece('G', 1), self.game.invalid_color())

    def test_place_invalid_piece(self):
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 1)
        self.assertEqual(self.game.invalid_placement(), "Sorry! Can't place a piece there, please try another move.")
        self.assertEqual(self.game.place_piece('B', 1), self.game.invalid_placement())
        self.assertEqual(self.game.place_piece('B', 8), self.game.invalid_placement())
        self.assertEqual(self.game.place_piece('B', ''), self.game.invalid_placement())

    def test_evaluate_rows_black_wins(self):
        self.game.place_piece('B', 1)
        self.game.place_piece('B', 2)
        self.game.place_piece('B', 3)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.game.place_piece('B', 4)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), 'Black')

    def test_evaluate_rows_red_wins(self):
        self.game.place_piece('R', 7)
        self.game.place_piece('R', 6)
        self.game.place_piece('R', 5)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.game.place_piece('R', 4)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), 'Red')

    def test_evaluate_columns_black_wins(self):
        self.game.place_piece('B', 6)
        self.game.place_piece('R', 6)
        self.game.place_piece('B', 7)
        self.game.place_piece('B', 7)
        self.game.place_piece('B', 7)
        aggregated = self.game.aggregate_columns()
        self.assertEqual(self.game.evaluate_sections('columns', aggregated), '')
        for column in aggregated[0:-2]:
            self.assertEqual(column, self.empty_column)
        self.assertEqual(aggregated[-2], ['|   ', '|   ', '|   ', '|   ', '| R ', '| B |'])
        self.assertEqual(aggregated[-1], ['|   ', '|   ', '|   ', '| B ', '| B ', '| B |'])
        self.game.place_piece('B', 7)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), 'Black')

    def test_evaluate_columns_red_wins(self):
        self.game.place_piece('R', 1)
        self.game.place_piece('R', 1)
        self.game.place_piece('R', 1)
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), '')
        self.game.place_piece('R', 1)
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), 'Red')

    def test_evaluate_diagonals_black_wins(self):
        aggregated = self.game.aggregate_diagonals()
        for agg in aggregated:
            self.assertEqual(type(agg), list)
        self.game.place_piece('R', 5)
        self.game.place_piece('B', 5)
        self.game.place_piece('B', 5)
        self.game.place_piece('B', 7)
        self.game.place_piece('R', 6)
        self.game.place_piece('B', 6)
        self.game.place_piece('B', 4)
        self.game.place_piece('R', 4)
        self.game.place_piece('B', 4)
        aggregated = self.game.aggregate_diagonals()
        self.assertEqual(self.game.evaluate_sections('diagonals', aggregated), '')
        self.game.place_piece('B', 4)
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), 'Black')

    def test_evaluate_diagonals_red_wins(self):
        self.game.place_piece('B', 3)
        self.game.place_piece('B', 3)
        self.game.place_piece('R', 3)
        self.game.place_piece('R', 1)
        self.game.place_piece('B', 2)
        self.game.place_piece('R', 2)
        self.game.place_piece('B', 4)
        self.game.place_piece('R', 4)
        self.game.place_piece('R', 4)
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), '')
        self.game.place_piece('R', 4)
        # print("\n")
        # self.game.render_board()
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), 'Red')

    def test_draw(self):
        self.assertEqual(self.game.draw(), 'Uh oh! No more slots open... game over!!')
        self.assertEqual(self.game.board_full(), False)
        for i in range(len(self.empty_row)):
            self.game.place_piece('R', (i + 1))
            self.game.place_piece('B', (i + 1))
            self.game.place_piece('R', (i + 1))
            self.game.place_piece('B', (i + 1))
            self.game.place_piece('R', (i + 1))
            self.game.place_piece('B', (i + 1))
        self.assertEqual(self.game.board_full(), True)
        self.assertEqual(self.game.place_piece('R', 1), self.game.draw())

    def test_game_over(self):
        self.game.place_piece('B', 1)
        self.game.place_piece('B', 2)
        self.game.place_piece('B', 3)
        self.assertEqual(self.game.game_over(), False)
        self.assertEqual(self.game.winner, '')
        self.game.place_piece('B', 4)
        self.assertEqual(self.game.game_over(), True)
        self.assertEqual(self.game.winner, 'Black')

if __name__ == '__main__':
    unittest.main()
