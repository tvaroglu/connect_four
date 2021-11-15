import unittest
from lib.prompt import Prompt
from lib.player import Player

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt()
        self.player_1 = Player('John', 'R')
        self.player_2 = Player('Jane', 'B')

    def test_welcome(self):
        self.assertEqual(self.prompt.welcome(), 'Welcome to ConnectFour!')

    def test_request_name(self):
        self.assertEqual(self.prompt.request_name(), "What is your name?\n > ")

    def test_greet_player(self):
        self.assertEqual(self.prompt.greet_player(self.player_1.name, self.player_1.full_color()), f"Welcome, {self.player_1.name}! Your color is '{self.player_1.full_color()}'")
        self.assertEqual(self.prompt.greet_player(self.player_2.name, self.player_2.full_color()), f"Welcome, {self.player_2.name}! Your color is '{self.player_2.full_color()}'")


if __name__ == '__main__':
    unittest.main()
