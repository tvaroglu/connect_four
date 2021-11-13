class Game:
    def __init__(self, board):
        self.board = board
        self.game_rows = (12, 10, 8, 6, 4, 2)
        self.valid_positions = ('|   ', '|   |')
        self.valid_colors = ('B', 'R')
        self.black_wins = '| B | B | B | B |'
        self.red_wins = '| R | R | R | R |'

    def invalid_placement(self):
        return "Sorry! Can't place a piece there, please try another move."

    def invalid_color(self):
        return 'Sorry! Invalid color, please try again.'

    def piece_placed(self):
        return 'Nice move!'

    def place_piece(self, color, column_number, row_index=0):
        column_index = int(column_number) - 1
        if row_index > 5 or column_index not in range(0, 7):
            return self.invalid_placement()
        elif color not in self.valid_colors:
            return self.invalid_color()
        row_placement = self.game_rows[row_index]
        net_placement = self.board[row_placement][column_index]
        if net_placement == self.valid_positions[0]:
            self.board[row_placement][column_index] = f'| {color} '
            return self.piece_placed()
        elif net_placement == self.valid_positions[1]:
            self.board[row_placement][column_index] = f'| {color} |'
            return self.piece_placed()
        return self.place_piece(color, column_number, row_index + 1)

    def evaluate_rows(self):
        winning_color = ''
        for row in self.board[2:-1]:
            joined = self.join_row(row)
            if self.black_wins in joined:
                winning_color = 'Black'
            elif self.red_wins in joined:
                winning_color = 'Red'
        return winning_color

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

    def evaluate_columns(self, aggregated_columns):
        winning_color = ''
        for column in aggregated_columns:
            column[-1] = self.reformat_last_cell(column[-1])
            joined = self.join_row(column)
            if self.black_wins in joined:
                winning_color = 'Black'
            elif self.red_wins in joined:
                winning_color = 'Red'
        return winning_color

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

    def evaluate_diagonals(self, aggregated_diagonals):
        winning_color = ''
        for diagonal in aggregated_diagonals:
            joined = self.join_row(diagonal)
            if self.black_wins in joined:
                winning_color = 'Black'
            elif self.red_wins in joined:
                winning_color = 'Red'
        return winning_color

    def reformat_last_cell(self, cell):
        return f'{cell}|'

    def join_row(self, row):
        return ''.join(row)

    def render_board(self):
        print(self.board[0])
        for row in self.board[1:len(self.board)]:
            print(self.join_row(row))
