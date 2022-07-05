class Prompt:
    def __init__(self):
        self.default_request = 'y'

    def welcome(self):
        return 'Welcome to ConnectFour!'

    def request_name(self):
        return "What is your name?\n > "

    def greet_player(self, player_name, player_color):
        return f"Welcome, {player_name}! Your color is '{player_color}'.\n You can (q)uit any time you'd like."

    def request_placement(self, player_name):
        return f"Your turn, {player_name}. Please enter a number between 1 and 7 to place a piece into the board:\n > "

    def line_break(self):
        return "\n"

    def start_game(self):
        return "Let's play!"

    def new_game(self):
        return "Would you like to play again? (y/n)\n > "

    def end_game(self):
        return "Game exiting...\n Goodbye!"

    def announce_victor(self, winning_color):
        return f'{winning_color} wins!!'

    def sanitize_request(self, user_input):
        return str(user_input.lower()[0])

    def request_game_mode(self):
        return "Please select game mode\n((1) vs (2) player):\n > "

    def game_mode(self, selection='1'):
        if str(selection) != '2':
            selection = '1'
        return f'Entering {selection}-player game mode'
