class Game:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.game_rows = (12, 10, 8, 6, 4, 2)
        self.valid_positions = ('|   ', '|   |')
        self.valid_colors = ('B', 'R')
        self.black_wins = '| B | B | B | B |'
        self.red_wins = '| R | R | R | R |'
        self.winner = ''

    def invalid_placement(self):
        return "Sorry! Can't place a piece there, please try another move."

    def invalid_color(self):
        return 'Sorry! Invalid color, please try again.'

    def piece_placed(self):
        return 'Nice move!'

    def draw(self):
        return 'Uh oh! No more slots open... game over!!'

    def board_full(self):
        return self.valid_positions[0] not in self.board[2] and self.valid_positions[1] not in self.board[2]

    def place_piece(self, color, column_number, row_index=0):
        try:
            column_index = int(column_number) - 1
        except ValueError:
            return self.invalid_placement()
        if row_index > 5 or column_index not in range(0, len(self.board[2])):
            return self.invalid_placement()
        elif color not in self.valid_colors:
            return self.invalid_color()
        elif self.board_full():
            return self.draw()
        row_placement = self.game_rows[row_index]
        net_placement = self.board[row_placement][column_index]
        formatted = self.format_cell(color)
        if net_placement == self.valid_positions[0]:
            self.board[row_placement][column_index] = formatted
        elif net_placement == self.valid_positions[1]:
            self.board[row_placement][column_index] = self.reformat_last_cell(formatted)
        return self.piece_placed() if net_placement in self.valid_positions else self.place_piece(color, column_number, row_index + 1)

    def aggregate_columns(self):
        col_1 = []
        col_2 = []
        col_3 = []
        col_4 = []
        col_5 = []
        col_6 = []
        col_7 = []
        for index, row in enumerate(self.board):
            if index in self.game_rows:
                col_1.append(row[0])
                col_2.append(row[1])
                col_3.append(row[2])
                col_4.append(row[3])
                col_5.append(row[4])
                col_6.append(row[5])
                col_7.append(row[6][0:-1])
        return (col_1, col_2, col_3, col_4, col_5, col_6, col_7)

    def aggregate_diagonals(self):
        up_1 = [self.board[8][0], self.board[6][1], self.board[4][2], self.reformat_last_cell(self.board[2][3])]
        up_2 = [self.board[10][0], self.board[8][1], self.board[6][2], self.board[4][3], self.reformat_last_cell(self.board[2][4])]
        up_3 = [self.board[12][0], self.board[10][1], self.board[8][2], self.board[6][3], self.board[4][4], self.reformat_last_cell(self.board[2][5])]
        up_4 = [self.board[12][1], self.board[10][2], self.board[8][3], self.board[6][4], self.board[4][5], self.board[2][6]]
        up_5 = [self.board[12][2], self.board[10][3], self.board[8][4], self.board[6][5], self.board[4][6]]
        up_6 = [self.board[12][3], self.board[10][4], self.board[8][5], self.board[6][6]]
        down_1 = [self.board[6][0], self.board[8][1], self.board[10][2], self.reformat_last_cell(self.board[12][3])]
        down_2 = [self.board[4][0], self.board[6][1], self.board[8][2], self.board[10][3], self.reformat_last_cell(self.board[12][4])]
        down_3 = [self.board[2][0], self.board[4][1], self.board[6][2], self.board[8][3], self.board[10][4], self.reformat_last_cell(self.board[12][5])]
        down_4 = [self.board[2][1], self.board[4][2], self.board[6][3], self.board[8][4], self.board[10][5], self.board[12][6]]
        down_5 = [self.board[2][2], self.board[4][3], self.board[6][4], self.board[8][5], self.board[10][6]]
        down_6 = [self.board[2][3], self.board[4][4], self.board[6][5], self.board[8][6]]
        return (up_1, up_2, up_3, up_4, up_5, up_6, down_1, down_2, down_3, down_4, down_5, down_6)

    def evaluate_sections(self, type, aggregated_sections, winning_color=''):
        for section in aggregated_sections:
            if type == 'columns':
                section[-1] = self.reformat_last_cell(section[-1])
            joined = self.join_row(section)
            if self.black_wins in joined:
                winning_color = 'Black'
            elif self.red_wins in joined:
                winning_color = 'Red'
        return winning_color

    def format_cell(self, color):
        return f'| {color} '

    def reformat_last_cell(self, cell):
        return f'{cell}|'

    def join_row(self, row):
        return ''.join(row)

    def set_winner(self):
        helper_dict = {
            'rows': self.evaluate_sections('rows', self.board),
            'columns': self.evaluate_sections('columns', self.aggregate_columns()),
            'diagonals': self.evaluate_sections('diagonals', self.aggregate_diagonals())
        }
        if 'Black' in helper_dict.values():
            self.winner = 'Black'
        elif 'Red' in helper_dict.values():
            self.winner = 'Red'

    def game_over(self):
        self.set_winner()
        return self.winner != '' or self.board_full()

    def render_board(self):
        print(self.board[0])
        for row in self.board[1:len(self.board)]:
            print(self.join_row(row))
