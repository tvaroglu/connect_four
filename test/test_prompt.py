import unittest
from lib.prompt import Prompt
from lib.player import Player

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt()
        self.red_piece = '🟥'
        self.black_piece = '⬛️'
        self.player_1 = Player('John', self.red_piece)
        self.player_2 = Player('Jane', self.black_piece)

    def test_welcome(self):
        self.assertEqual(self.prompt.welcome(), 'Welcome to ConnectFour!')

    def test_request_name(self):
        self.assertEqual(self.prompt.request_name(), "What is your name?\n > ")

    def test_greet_player(self):
        self.assertEqual(self.prompt.greet_player(self.player_1.name, self.player_1.full_color()), f"Welcome, {self.player_1.name}! Your color is '{self.player_1.full_color()}'.\n You can (q)uit any time you'd like.")
        self.assertEqual(self.prompt.greet_player(self.player_2.name, self.player_2.full_color()), f"Welcome, {self.player_2.name}! Your color is '{self.player_2.full_color()}'.\n You can (q)uit any time you'd like.")

    def test_request_placement(self):
        self.assertEqual(self.prompt.request_placement(self.player_1.name), f"Your turn, {self.player_1.name}. Please enter a number between 1 and 7 to place a piece into the board:\n > ")
        self.assertEqual(self.prompt.request_placement(self.player_2.name), f"Your turn, {self.player_2.name}. Please enter a number between 1 and 7 to place a piece into the board:\n > ")

    def test_line_break(self):
        self.assertEqual(self.prompt.line_break(), "\n")

    def test_start_game(self):
        self.assertEqual(self.prompt.start_game(), "Let's play!")

    def test_new_game(self):
        self.assertEqual(self.prompt.new_game(), "Would you like to play again? (y/n)\n > ")

    def test_end_game(self):
        self.assertEqual(self.prompt.end_game(), "Game exiting...\n Goodbye!")

    def test_announce_victor(self):
        self.assertEqual(self.prompt.announce_victor(self.player_1.full_color()), f"{self.player_1.full_color()} wins!!")

    def test_sanitize_request(self):
        user_input = 'NO'
        self.assertEqual(self.prompt.sanitize_request(user_input), 'n')
        self.assertEqual(self.prompt.default_request, 'y')

    def test_request_game_mode(self):
        self.assertEqual(self.prompt.request_game_mode(), "Please select game mode\n((1) vs (2) player):\n > ")

    def test_game_mode(self):
        self.assertEqual(self.prompt.game_mode(), f'Entering 1-player game mode')
        self.assertEqual(self.prompt.game_mode(2), f'Entering 2-player game mode')
        self.assertEqual(self.prompt.game_mode(1), f'Entering 1-player game mode')
        self.assertEqual(self.prompt.game_mode('dfsasfsf'), f'Entering 1-player game mode')


if __name__ == '__main__':
    unittest.main(verbosity=2)
