class Turn:
    def __init__(self, board):
        self.board = board
        self.game_rows = (12, 10, 8, 6, 4, 2)
        self.valid_positions = ('|   ', '|   |')
        self.valid_colors = ('B', 'R')

    def invalid_placement(self):
        return "Sorry! Can't place a piece there, please try another move."

    def invalid_color(self):
        return 'Sorry! Invalid color, please try again.'

    def place_piece(self, color, column_number, row_index=0):
        column_index = int(column_number) - 1
        if row_index > 5 or column_index not in range(0, 7):
            print(self.invalid_placement())
        elif color not in self.valid_colors:
            print(self.invalid_color())
        else:
            row_placement = self.game_rows[row_index]
            net_placement = self.board[row_placement][column_index]
            if net_placement == self.valid_positions[0]:
                self.board[row_placement][column_index] = f'| {color} '
            elif net_placement == self.valid_positions[1]:
                self.board[row_placement][column_index] = f'| {color} |'
            else:
                return self.place_piece(color, column_number, row_index + 1)

    def evaluate_rows(self):
        winning_color = ''
        black_wins = '| B | B | B | B |'
        red_wins = '| R | R | R | R |'
        for row in self.board[2:-1]:
            joined = self.join_row(row)
            if black_wins in joined:
                winning_color = 'Black'
            elif red_wins in joined:
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
        black_wins = '| B | B | B | B |'
        red_wins = '| R | R | R | R |'
        for column in aggregated_columns:
            column[-1] = f'{column[-1]}|'
            joined = self.join_row(column)
            if black_wins in joined:
                winning_color = 'Black'
            elif red_wins in joined:
                winning_color = 'Red'
        return winning_color

    def join_row(self, row):
        return ''.join(row)

    def render_board(self):
        print(self.board[0])
        for row in self.board[1:len(self.board)]:
            print(self.join_row(row))
