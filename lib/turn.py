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

    def join_row(self, row):
        return ''.join(row)

    def render_board(self):
        print(self.board[0])
        for row in self.board[1:len(self.board)]:
            print(self.join_row(row))
