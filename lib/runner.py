from lib.board import Board
from lib.player import Player
from lib.game import Game
from lib.prompt import Prompt

def run_game(new_game='y', forfeit=False):
    while new_game == 'y' and forfeit == False:
        board, prompt = Board(), Prompt()
        print(prompt.welcome())
        print(prompt.line_break())
        # select 1 vs 2 player mode:
        game_mode = input(prompt.request_game_mode())
        print(prompt.game_mode(game_mode))
        print(prompt.line_break())
        # request player 1 name:
        name = input(prompt.request_name())
        player_1 = Player(name, board.red_piece)
        print(prompt.greet_player(player_1.name, player_1.full_color()))
        print(prompt.line_break())
        # request player 2 name (if not 1-player mode):
        if game_mode == '2':
            name = input(prompt.request_name())
        else:
            name = player_1.default_name
        player_2 = Player(name, board.black_piece)
        print(prompt.greet_player(player_2.name, player_2.full_color()))
        print(prompt.line_break())
        # initialize game board:
        game = Game(board.construct_board(), player_1, player_2)
        print(prompt.start_game())
        # collect player 1 input:
        while not game.game_over() and not forfeit:
            print(prompt.line_break())
            game.render_board()
            print(prompt.line_break())
            turn = input(prompt.request_placement(player_1.name))
            result = game.place_piece(player_1.color, turn)
            while result not in (game.piece_placed(), game.forfeit()):
                print(result)
                print(prompt.line_break())
                turn = input(prompt.request_placement(player_1.name))
                result = game.place_piece(player_1.color, turn)
            print(result)
            if result != game.forfeit():
                print(prompt.line_break())
                game.render_board()
            else:
                forfeit = True
            # collect player 2 input:
            if not game.game_over() and not forfeit:
                print(prompt.line_break())
                if game_mode == '2':
                    turn = input(prompt.request_placement(player_2.name))
                    result = game.place_piece(player_2.color, turn)
                else:
                    result = game.place_piece(player_2.color, game.skynet_turn(turn))
                while result not in (game.piece_placed(), game.forfeit()):
                    if game_mode == '2':
                        print(result)
                        print(prompt.line_break())
                        turn = input(prompt.request_placement(player_2.name))
                        result = game.place_piece(player_2.color, turn)
                    else:
                        result = game.place_piece(player_2.color, game.skynet_turn(turn))
                print(result)
                game.game_over()
        # Announce game results:
        print(prompt.line_break())
        if not forfeit:
            game.render_board()
            print(prompt.line_break())
            if game.board_full():
                print(game.draw())
            else:
                print(prompt.announce_victor(game.winner))
        # Request input for replay:
        request = input(prompt.new_game())
        forfeit = False
        if len(request) == 0:
            new_game = prompt.default_request
        else:
            new_game = prompt.sanitize_request(request)
    # Exit game flow:
    print(prompt.line_break())
    print(prompt.end_game())
