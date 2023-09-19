import unittest
from lib.board import Board
from lib.player import Player
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.red_piece   = self.board.red_piece
        self.black_piece = self.board.black_piece
        self.player_1 = Player(self.red_piece, 'John')
        self.player_2 = Player(self.black_piece, 'Jane')
        self.game = Game(self.board, self.player_1, self.player_2)

    def test_place_piece(self):
        invalid_placement = self.game.place_piece(
            self.board.red_piece, 0, skynet_turn=True)
        self.assertFalse(invalid_placement)
        invalid_placement = self.game.place_piece(
            self.board.red_piece, 8, skynet_turn=True)
        self.assertFalse(invalid_placement)

    def test_game_over(self):
        self.assertFalse(self.game.game_over())
        for idx, col in enumerate(self.game.board.grid):
            for sub_idx, slot in enumerate(col):
                self.game.place_piece(
                    self.board.red_piece if sub_idx % 2 == 0 \
                        else self.board.black_piece, idx + 1, skynet_turn=True)
        # self.board.print_board()
        self.assertTrue(self.game.game_over())


if __name__ == '__main__':
    unittest.main()
