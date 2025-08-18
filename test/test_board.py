import unittest
from lib.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_color(self):
        default_piece = self.board.default
        self.assertEqual(default_piece, self.board.get_color(default_piece))
        red_piece = self.board.red_piece
        self.assertEqual('red', self.board.get_color(red_piece))
        blue_piece = self.board.blue_piece
        self.assertEqual('blue', self.board.get_color(blue_piece))

    def test_get_piece(self):
        default_piece = self.board.default
        self.assertEqual(default_piece, self.board.get_piece(default_piece))
        red_piece = self.board.red_piece
        self.assertEqual(red_piece, self.board.get_piece(red_piece))
        blue_piece = self.board.blue_piece
        self.assertEqual(blue_piece, self.board.get_piece(blue_piece))

    def test_place_piece(self):
        invalid_placement = self.board.place_piece(self.board.red_piece, 7)
        self.assertFalse(invalid_placement)
        valid_placement = self.board.place_piece(self.board.red_piece, 0)
        self.assertTrue(valid_placement)
        self.board.place_piece(self.board.blue_piece, 0)
        self.assertEqual(self.board.grid[0][0], self.board.red_piece)
        self.assertEqual(self.board.grid[0][1], self.board.blue_piece)

    def test_eval_columns(self):
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.blue_piece, 0)
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.blue_piece, 0)
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.blue_piece, 0)
        self.board.place_piece(self.board.red_piece, 1)
        # self.board.render_board()
        self.assertEqual(self.board.eval_columns(), ('red', 1))
        self.assertEqual(self.board.eval(), 'red')

    def test_eval_rows(self):
        self.board.place_piece(self.board.blue_piece, 0)
        self.board.place_piece(self.board.red_piece, 0)
        self.board.place_piece(self.board.blue_piece, 1)
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.blue_piece, 2)
        self.board.place_piece(self.board.red_piece, 2)
        self.board.place_piece(self.board.blue_piece, 3)
        # self.board.render_board()
        # self.assertEqual(self.board.eval_rows(), ('blue', 4))
        self.assertEqual(self.board.eval_rows(), ('blue', None))
        self.assertEqual(self.board.eval(), 'blue')

    def test_eval_diagonals_top_right(self):
        self.board.place_piece(self.board.blue_piece, 0)
        self.board.place_piece(self.board.red_piece, 1)
        self.board.place_piece(self.board.blue_piece, 1)
        self.board.place_piece(self.board.red_piece, 2)
        self.board.place_piece(self.board.blue_piece, 2)
        self.board.place_piece(self.board.red_piece, 3)
        self.board.place_piece(self.board.blue_piece, 2)
        self.board.place_piece(self.board.red_piece, 3)
        self.board.place_piece(self.board.blue_piece, 3)
        self.board.place_piece(self.board.red_piece, 2)
        self.board.place_piece(self.board.blue_piece, 3)
        # self.board.render_board()
        self.assertEqual(self.board.eval_diagonals(), ('blue', None))
        self.assertEqual(self.board.eval(), 'blue')

    def test_eval_diagonals_top_left(self):
        self.board.place_piece(self.board.blue_piece, 6)
        self.board.place_piece(self.board.red_piece, 5)
        self.board.place_piece(self.board.blue_piece, 5)
        self.board.place_piece(self.board.red_piece, 4)
        self.board.place_piece(self.board.blue_piece, 4)
        self.board.place_piece(self.board.red_piece, 3)
        self.board.place_piece(self.board.blue_piece, 4)
        self.board.place_piece(self.board.red_piece, 3)
        self.board.place_piece(self.board.blue_piece, 3)
        self.board.place_piece(self.board.red_piece, 4)
        self.board.place_piece(self.board.blue_piece, 3)
        # self.board.render_board()
        self.assertEqual(self.board.eval_diagonals(), ('blue', None))
        self.assertEqual(self.board.eval(), 'blue')

    def test_eval_draw(self):
        for idx, col in enumerate(self.board.grid):
            for x in range(0, len(col) + 1):
                if idx % 2 == 0:
                    self.board.place_piece(self.board.blue_piece, x)
                else:
                    self.board.place_piece(self.board.red_piece, x)
        # self.board.render_board()
        self.assertEqual(self.board.eval(), 'draw')


if __name__ == '__main__':
    unittest.main()
