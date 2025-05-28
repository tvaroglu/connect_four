import random
# import time
from lib.prompt import Prompt

class Game:

    def __init__(self, board, player_1, player_2,
                 test_mode=False) -> None:
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.test_mode = test_mode
        self.prompt = Prompt(test_mode=test_mode)

    def place_piece(self, color, column_number, skynet_turn=False):
        result = None
        try:
            column_idx = int(column_number)
            if not skynet_turn: column_idx -= 1
            if column_idx >= 0: result = self.board.place_piece(color, column_idx)
        except (ValueError, IndexError):
            result = None
        prompt = self.prompt.piece_placed() if result else self.prompt.invalid_placement()
        if not skynet_turn: print(prompt)
        if result:
            if skynet_turn: self.prompt._assimilating
            return True
        return False

    # TODO: consider UX enhancement to highlight winning sequence
    def game_over(self):
        result = self.board.eval()
        return False if not result and result != 'draw' else True

    def run(self, game_mode):
        print(self.prompt.start_game())
        while not self.game_over():
            self.board.render_board()
            result, placement = self.human_turn(self.player_1.name, self.player_1.color)
            while not result:
                result, placement = self.human_turn(self.player_1.name, self.player_1.color)
            self.board.render_board()
            if not self.game_over():
                if game_mode == '2':  # 2 players
                    result, placement = self.human_turn(self.player_2.name, self.player_2.color)
                else:  # 1 player
                    result = self.skynet_turn(placement)
                while not result:
                    if game_mode == '2':  # 2 players
                        result, placement = self.human_turn(self.player_2.name, self.player_2.color)
                    else:  # 1 player
                        result = self.skynet_turn(placement)
                self.game_over()
        self.board.render_board()
        result = self.board.eval()
        if result == 'draw': print(self.prompt.draw())
        else: print(self.prompt.announce_victor(result))

    def human_turn(self, name, color):
        result = placement = None
        placement = input(self.prompt.request_placement(name))
        result = self.place_piece(color, placement)
        return result, placement

    def skynet_turn(self, player_input, eval_color='red'):
        result = placement = None
        selection = self.board.eval(seq_number=3, eval_color=eval_color)
        if selection is None:
            floor, ciel = -2, 0  # -1, 1
            input = int(player_input)
            selection = random.choice([(input + floor), (input + ciel)])
        # print('selection: ', selection)
        # return selection
        result = self.place_piece(self.player_2.color, selection, skynet_turn=True)
        return result
