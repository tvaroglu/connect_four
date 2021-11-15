from lib.board import Board
from lib.player import Player
from lib.game import Game
from lib.prompt import Prompt

prompt = Prompt()
print(prompt.welcome())

player_1_name = input(prompt.request_name())
player_1 = Player(player_1_name, 'R')
print(player_1.greet())

player_2_name = input(prompt.request_name())
player_2 = Player(player_2_name, 'B')
print(player_2.greet())
