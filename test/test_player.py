import unittest
from lib.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.red_piece   = '🟥'
        self.blue_piece = '🟦'
        self.player_1 = Player(self.red_piece, 'John')
        self.player_2 = Player(self.blue_piece, 'Sarah')
        self.default_player = Player(self.blue_piece)

    def test_attributes(self):
        self.assertEqual(self.player_1.name, 'John')
        self.assertEqual(self.player_2.name, 'Sarah')
        self.assertEqual(self.player_1.color, self.red_piece)
        self.assertEqual(self.player_2.color, self.blue_piece)
        self.assertEqual(self.default_player.name, 'Skynet')

    def test_full_color(self):
        self.assertEqual(self.player_1.full_color(), 'Red')
        self.assertEqual(self.player_2.full_color(), 'Blue')
        self.assertEqual(self.default_player.full_color(), 'Blue')


if __name__ == '__main__':
    unittest.main()
