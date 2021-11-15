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

    def test_greeting(self):
        self.assertEqual(self.player_1.full_color(), 'Red')
        self.assertEqual(self.player_2.full_color(), 'Black')
        self.assertEqual(self.player_1.greet(), f"Welcome, {self.player_1.name}! Your color is '{self.player_1.full_color()}'")
        self.assertEqual(self.player_2.greet(), f"Welcome, {self.player_2.name}! Your color is '{self.player_2.full_color()}'")


if __name__ == '__main__':
    unittest.main()
