class Prompt:
    def __init__(self):
        pass

    def welcome(self):
        return 'Welcome to ConnectFour!'

    def request_name(self):
        return "What is your name?\n > "

    def greet_player(self, player_name, player_color):
        return f"Welcome, {player_name}! Your color is '{player_color}'"
