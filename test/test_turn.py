import unittest
from lib.board import Board
from lib.turn import Turn

class TestTurn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.full_board = self.board.construct_board()
        self.turn = Turn(self.full_board)
        self.sample_row = self.turn.board[self.turn.game_rows[0]]

    def test_game_rows(self):
        empty_row = ['|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   |']
        for index in self.turn.game_rows:
            self.assertEqual(self.turn.board[index], empty_row)
