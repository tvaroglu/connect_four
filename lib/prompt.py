class Prompt:
    def __init__(self):
        pass

    def welcome(self):
        return 'Welcome to ConnectFour!'

    def request_name(self):
        return "What is your name?\n > "

    def greet_player(self, player_name, player_color):
        return f"Welcome, {player_name}! Your color is '{player_color}'"

    def request_placement(self, player_name):
        return f"Your turn, {player_name}. Please enter a number between 1 and 7 to place a piece into the board:\n > "

    def line_break(self):
        return "\n"

    def announce_victor(self, winning_color):
        return f'{winning_color} wins!'
