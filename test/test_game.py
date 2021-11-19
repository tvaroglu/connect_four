import unittest
from lib.board import Board
from lib.player import Player
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.red_piece = self.board.red_piece
        self.black_piece = self.board.black_piece
        self.player_1 = Player('John', self.red_piece)
        self.player_2 = Player('Jane', self.black_piece)
        self.game = Game(self.board.construct_board(), self.player_1, self.player_2)
        self.first_row = self.game.board[self.game.game_rows[0]]
        self.second_row = self.game.board[self.game.game_rows[1]]
        self.empty_row = ['|    ', '|    ', '|    ', '|    ', '|    ', '|    ', '|    |']
        self.empty_column = ['|    ', '|    ', '|    ', '|    ', '|    ', '|    |']

    def test_join_row(self):
        self.assertEqual(self.game.join_row(self.empty_row), '|    |    |    |    |    |    |    |')
        self.assertEqual(self.game.join_row(self.empty_column), '|    |    |    |    |    |    |')

    def test_game_rows(self):
        for index in self.game.game_rows:
            self.assertEqual(self.game.board[index], self.empty_row)
            self.assertEqual(len(self.game.board[index]), 7)

    def test_piece_placed(self):
        self.assertEqual(self.game.piece_placed(), 'Nice move!')

    def test_place_valid_piece(self):
        self.assertEqual(self.first_row[0], '|    ')
        self.assertEqual(self.game.place_piece(self.red_piece, 1), self.game.piece_placed())
        self.assertEqual(self.first_row[0], '| 🟥 ')
        self.game.place_piece(self.red_piece, 1)
        self.assertEqual(self.second_row[0], '| 🟥 ')
        self.assertEqual(self.first_row[6], '|    |')
        self.game.place_piece(self.black_piece, 7)
        self.assertEqual(self.first_row[6], '| ⬛️ |')
        self.game.place_piece(self.black_piece, 7)
        self.assertEqual(self.second_row[6], '| ⬛️ |')

    def test_reformat_last_cell(self):
        formatted = self.game.format_cell(self.red_piece)
        self.assertEqual(formatted, '| 🟥 ')
        self.assertEqual(self.game.reformat_last_cell(formatted), '| 🟥 |')

    def test_place_invalid_piece(self):
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.black_piece, 1)
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.black_piece, 1)
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.black_piece, 1)
        self.assertEqual(self.game.invalid_placement(), "Sorry! Can't place a piece there, please try another move.")
        self.assertEqual(self.game.place_piece(self.black_piece, 1), self.game.invalid_placement())
        self.assertEqual(self.game.place_piece(self.black_piece, 8), self.game.invalid_placement())
        self.assertEqual(self.game.place_piece(self.black_piece, ''), self.game.invalid_placement())

    def test_evaluate_rows_black_wins(self):
        self.game.place_piece(self.black_piece, 1)
        self.game.place_piece(self.black_piece, 2)
        self.game.place_piece(self.black_piece, 3)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.game.place_piece(self.black_piece, 4)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), 'Black')

    def test_evaluate_rows_red_wins(self):
        self.game.place_piece(self.red_piece, 7)
        self.game.place_piece(self.red_piece, 6)
        self.game.place_piece(self.red_piece, 5)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.game.place_piece(self.red_piece, 4)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), 'Red')

    def test_evaluate_columns_black_wins(self):
        self.game.place_piece(self.black_piece, 6)
        self.game.place_piece(self.red_piece, 6)
        self.game.place_piece(self.black_piece, 7)
        self.game.place_piece(self.black_piece, 7)
        self.game.place_piece(self.black_piece, 7)
        aggregated = self.game.aggregate_columns()
        self.assertEqual(self.game.evaluate_sections('columns', aggregated), '')
        for column in aggregated[0:-2]:
            self.assertEqual(column, self.empty_column)
        self.assertEqual(aggregated[-2], ['|    ', '|    ', '|    ', '|    ', '| 🟥 ', '| ⬛️ |'])
        self.assertEqual(aggregated[-1], ['|    ', '|    ', '|    ', '| ⬛️ ', '| ⬛️ ', '| ⬛️ |'])
        self.game.place_piece(self.black_piece, 7)
        self.assertEqual(self.game.evaluate_sections('rows', self.game.board), '')
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), 'Black')

    def test_evaluate_columns_red_wins(self):
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.red_piece, 1)
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), '')
        self.game.place_piece(self.red_piece, 1)
        self.assertEqual(self.game.evaluate_sections('columns', self.game.aggregate_columns()), 'Red')

    def test_evaluate_diagonals_black_wins(self):
        aggregated = self.game.aggregate_diagonals()
        for agg in aggregated:
            self.assertEqual(type(agg), list)
        self.game.place_piece(self.red_piece, 5)
        self.game.place_piece(self.black_piece, 5)
        self.game.place_piece(self.black_piece, 5)
        self.game.place_piece(self.black_piece, 7)
        self.game.place_piece(self.red_piece, 6)
        self.game.place_piece(self.black_piece, 6)
        self.game.place_piece(self.black_piece, 4)
        self.game.place_piece(self.red_piece, 4)
        self.game.place_piece(self.black_piece, 4)
        aggregated = self.game.aggregate_diagonals()
        self.assertEqual(self.game.evaluate_sections('diagonals', aggregated), '')
        self.game.place_piece(self.black_piece, 4)
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), 'Black')

    def test_evaluate_diagonals_red_wins(self):
        self.game.place_piece(self.black_piece, 3)
        self.game.place_piece(self.black_piece, 3)
        self.game.place_piece(self.red_piece, 3)
        self.game.place_piece(self.red_piece, 1)
        self.game.place_piece(self.black_piece, 2)
        self.game.place_piece(self.red_piece, 2)
        self.game.place_piece(self.black_piece, 4)
        self.game.place_piece(self.red_piece, 4)
        self.game.place_piece(self.red_piece, 4)
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), '')
        self.game.place_piece(self.red_piece, 4)
        # print("\n")
        # self.game.render_board()
        self.assertEqual(self.game.evaluate_sections('diagonals', self.game.aggregate_diagonals()), 'Red')

    def test_draw(self):
        self.assertEqual(self.game.draw(), 'Uh oh! No more slots open... game over!!')
        self.assertEqual(self.game.board_full(), False)
        for i in range(len(self.empty_row)):
            self.game.place_piece(self.red_piece, (i + 1))
            self.game.place_piece(self.black_piece, (i + 1))
            self.game.place_piece(self.red_piece, (i + 1))
            self.game.place_piece(self.black_piece, (i + 1))
            self.game.place_piece(self.red_piece, (i + 1))
            self.game.place_piece(self.black_piece, (i + 1))
        self.assertEqual(self.game.board_full(), True)
        self.assertEqual(self.game.place_piece(self.red_piece, 1), self.game.draw())

    def test_game_over(self):
        self.game.place_piece(self.black_piece, 1)
        self.game.place_piece(self.black_piece, 2)
        self.game.place_piece(self.black_piece, 3)
        self.assertEqual(self.game.game_over(), False)
        self.assertEqual(self.game.winner, '')
        self.game.place_piece(self.black_piece, 4)
        self.assertEqual(self.game.game_over(), True)
        self.assertEqual(self.game.winner, 'Black')


if __name__ == '__main__':
    unittest.main()
