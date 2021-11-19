from lib.board import Board
from lib.player import Player
from lib.game import Game
from lib.prompt import Prompt

def run_game(new_game='y'):
    while new_game == 'y':
        board = Board()
        prompt = Prompt()
        print(prompt.welcome())
        print(prompt.line_break())

        name = input(prompt.request_name())
        player_1 = Player(name, board.red_piece)
        print(prompt.greet_player(player_1.name, player_1.full_color()))
        print(prompt.line_break())

        name = input(prompt.request_name())
        player_2 = Player(name, board.black_piece)
        print(prompt.greet_player(player_2.name, player_2.full_color()))
        print(prompt.line_break())

        game = Game(board.construct_board(), player_1, player_2)
        print(prompt.start_game())

        while not game.game_over():
            print(prompt.line_break())
            game.render_board()
            print(prompt.line_break())
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
                print(prompt.line_break())
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
        game.render_board()
        print(prompt.line_break())
        if game.board_full():
            print(game.draw())
        else:
            print(prompt.announce_victor(game.winner))

        request = input(prompt.new_game())
        if len(request) == 0:
            new_game = prompt.default_request
        else:
            new_game = prompt.sanitize_request(request)

    print(prompt.line_break())
    print(prompt.end_game())
