from lib.board import Board
from lib.player import Player
from lib.game import Game
from lib.prompt import Prompt


prompt = Prompt()
print(prompt.welcome())
print(prompt.line_break())

name = input(prompt.request_name())
player_1 = Player(name, 'R')
print(prompt.greet_player(player_1.name, player_1.full_color()))
print(prompt.line_break())

name = input(prompt.request_name())
player_2 = Player(name, 'B')
print(prompt.greet_player(player_2.name, player_2.full_color()))
print(prompt.line_break())

board = Board()
game = Game(board.construct_board(), player_1, player_2)

while not game.game_over():
    print(prompt.line_break())
    game.render_board()
    turn = input(prompt.request_placement(player_1.name))
    result = game.place_piece(player_1.color, turn)
    while result != game.piece_placed():
        print(result)
        print(prompt.line_break())
        turn = input(prompt.request_placement(player_1.name))
        result = game.place_piece(player_1.color, turn)
    print(result)
    print(prompt.line_break())
    game.render_board()

    if not game.game_over():
        turn = input(prompt.request_placement(player_2.name))
        result = game.place_piece(player_2.color, turn)
        while result != game.piece_placed():
            print(result)
            print(prompt.line_break())
            turn = input(prompt.request_placement(player_2.name))
            result = game.place_piece(player_2.color, turn)
        print(result)
        game.game_over()

print(prompt.line_break())
print(prompt.announce_victor(game.winner))
