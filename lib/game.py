from lib.prompt import Prompt

class Game:

    def __init__(self, board, player_1, player_2) -> None:
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
        while not self.game_over():
            self.board.print_board()
            placement = input(self.prompt.request_placement(self.player_1.name))
            result = self.place_piece(self.player_1.color, placement)
            while not result:
                placement = input(self.prompt.request_placement(self.player_1.name))
                result = self.place_piece(self.player_1.color, placement)
            self.board.print_board()
            if not self.game_over():
                if game_mode == '2':
                    placement = input(self.prompt.request_placement(self.player_2.name))
                    result = self.place_piece(self.player_2.color, placement)
                else:
                    result = self.board.place_piece(
                        self.player_2.color, self.board.skynet_turn(placement))
                    self.prompt._assimilating
                while not result:
                    if game_mode == '2':
                        placement = input(self.prompt.request_placement(self.player_2.name))
                        result = self.place_piece(self.player_2.color, placement)
                    else:
                        result = self.board.place_piece(
                            self.player_2.color, self.board.skynet_turn(placement))
                        self.prompt._assimilating
                self.game_over()
        self.board.print_board()
        result = self.board.eval()
        if result == 'draw': print(self.prompt.draw())
        else: print(self.prompt.announce_victor(result))
