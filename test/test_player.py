import unittest
from lib.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player('John', 'R')
        self.player_2 = Player('Jane', 'B')

    def test_attributes(self):
        self.assertEqual(self.player_1.name, 'John')
        self.assertEqual(self.player_2.name, 'Jane')
        self.assertEqual(self.player_1.color, 'R')
        self.assertEqual(self.player_2.color, 'B')

    def test_full_color(self):
        self.assertEqual(self.player_1.full_color(), 'Red')
        self.assertEqual(self.player_2.full_color(), 'Black')


if __name__ == '__main__':
    unittest.main()
