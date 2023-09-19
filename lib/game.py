import random
# from prompt import Prompt
from lib.prompt import Prompt

class Game:

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.prompt = Prompt()

    def place_piece(self, color, column_number, skynet_turn=False):
        result = None
        try:
            column_idx = int(column_number) - 1
            if column_idx >= 0:
                result = self.board.place_piece(color, column_idx)
        except (ValueError, IndexError):
            result = None
        prompt = self.prompt.piece_placed() if result else self.prompt.invalid_placement()
        if not skynet_turn:
            print(prompt)
        return True if result else False

    def game_over(self):
        result = self.board.eval()
        return False if not result and result != 'draw' else True

    def run(self, game_mode):
        print(self.prompt.start_game())
        line_break = self.prompt.line_break()
        while not self.game_over():
            print(line_break)
            self.board.print_board()
            print(line_break)
            placement = input(self.prompt.request_placement(self.player_1.name))
            result = self.place_piece(self.player_1.color, placement)
            while not result:
                print(line_break)
                placement = input(self.prompt.request_placement(self.player_1.name))
                result = self.place_piece(self.player_1.color, placement)
            print(line_break)
            self.board.print_board()
            if not self.game_over():
                print(line_break)
                if game_mode == '2':
                    placement = input(self.prompt.request_placement(self.player_2.name))
                    result = self.place_piece(self.player_2.color, placement)
                else:
                    result = self.place_piece(
                        self.player_2.color, self.skynet_turn(placement), skynet_turn=True)
                while not result:
                    print(line_break)
                    if game_mode == '2':
                        placement = input(self.prompt.request_placement(self.player_2.name))
                        result = self.place_piece(self.player_2.color, placement)
                    else:
                        result = self.place_piece(
                            self.player_2.color, self.skynet_turn(placement), skynet_turn=True)
                self.game_over()
        print(line_break)
        self.board.print_board()
        print(line_break)
        result = self.board.eval()
        if result == 'draw':
            print(self.prompt.draw())
        else:
            print(self.prompt.announce_victor(result))
        print(line_break)

    # TODO: refactor and move to board class for more advanced difficulty level
    def skynet_turn(self, player_input):
        selection = random.choice(
            [(int(player_input) - 1), int(player_input), (int(player_input) + 1)])
        return selection
