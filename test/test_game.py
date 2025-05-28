import unittest
from lib.board import Board
from lib.player import Player
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.red_piece   = self.board.red_piece
        self.blue_piece = self.board.blue_piece
        self.player_1 = Player(self.red_piece, 'John')
        self.player_2 = Player(self.blue_piece, 'Sarah')
        self.game = Game(self.board, self.player_1, self.player_2,
                         test_mode=True)

    def test_place_piece(self):
        valid_placement = self.game.place_piece(
            self.board.red_piece, 0, skynet_turn=True)
        self.assertTrue(valid_placement)
        invalid_placement = self.game.place_piece(
            self.board.red_piece, 8, skynet_turn=True)
        self.assertFalse(invalid_placement)

    def test_game_over(self):
        self.assertFalse(self.game.game_over())
        for idx, col in enumerate(self.game.board.grid):
            for sub_idx, slot in enumerate(col):
                self.game.place_piece(
                    self.board.red_piece if sub_idx % 2 == 0 \
                        else self.board.blue_piece, idx + 1, skynet_turn=True)
        self.assertTrue(self.game.game_over())

    def test_skynet_turn_columns_result(self):
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.red_piece, 1)
        # self.board.render_board()
        self.assertEqual(self.game.skynet_turn(0), 1)

    def test_skynet_turn_rows_result(self):
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.red_piece, 2)
        self.board.place_piece(self.board.red_piece, 3)
        # self.board.render_board()
        self.assertTrue(self.game.skynet_turn(0))

    def test_skynet_turn_random_result(self):
        self.board.place_piece(self.board.red_piece, 1)
        # self.board.render_board()
        self.assertIn(self.game.skynet_turn(3), (1, 3))


if __name__ == '__main__':
    unittest.main()
