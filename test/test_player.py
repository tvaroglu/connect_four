import unittest
from lib.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.red_piece = '🟥'
        self.black_piece = '⬛️'
        self.player_1 = Player('John', self.red_piece)
        self.player_2 = Player('Jane', self.black_piece)

    def test_attributes(self):
        self.assertEqual(self.player_1.name, 'John')
        self.assertEqual(self.player_2.name, 'Jane')
        self.assertEqual(self.player_1.color, self.red_piece)
        self.assertEqual(self.player_2.color, self.black_piece)
        self.assertEqual(self.player_1.default_name, 'Skynet')

    def test_full_color(self):
        self.assertEqual(self.player_1.full_color(), 'Red')
        self.assertEqual(self.player_2.full_color(), 'Black')


if __name__ == '__main__':
    unittest.main()
