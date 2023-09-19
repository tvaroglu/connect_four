from lib.prompt import Prompt
from lib.board import Board
from lib.player import Player
from lib.game import Game

prompt = Prompt()
line_break = prompt.line_break()
new_game = 'y'

if __name__ == '__main__':
    while new_game == 'y':
        # greet the player(s):
        print(prompt.welcome())
        print(line_break)
        # request 1 vs 2-player mode:
        game_mode = input(prompt.request_game_mode())
        print(prompt.game_mode(game_mode))
        print(line_break)
        # request player 1 name:
        name = input(prompt.request_name())
        board = Board()
        player_1 = Player(board.red_piece, name)
        # announce player 1 name and color:
        print(prompt.greet_player(player_1.name, player_1.full_color()))
        print(line_break)
        # request player 2 name, if applicable:
        name = None
        if game_mode == '2':
            name = input(prompt.request_name())
        player_2 = Player(board.black_piece, name=name)
        # announce player 2 name and color:
        print(prompt.greet_player(player_2.name, player_2.full_color()))
        print(line_break)
        # run the game:
        game = Game(board, player_1, player_2)
        game.run(game_mode)
        # present option to replay game:
        request = input(prompt.new_game())
        new_game = prompt.default_request
        if len(request) > 0:
            new_game = prompt.sanitize_request(request)
    # end the game:
    print(line_break)
    print(prompt.end_game())
