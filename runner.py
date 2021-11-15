from lib.board import Board
from lib.player import Player
from lib.game import Game
from lib.prompt import Prompt

prompt = Prompt()
print(prompt.welcome())

name = input(prompt.request_name())
player_1 = Player(name, 'R')
print(prompt.greet_player(player_1.name, player_1.full_color()))

name = input(prompt.request_name())
player_2 = Player(name, 'B')
print(prompt.greet_player(player_2.name, player_2.full_color()))
