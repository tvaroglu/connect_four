class Turn:
    def __init__(self, board):
        self.board = board
        self.game_rows = (12, 10, 8, 6, 4, 2)
        self.valid_positions = ('|   ', '|   |')

    def invalid_placement(self):
        return "Sorry! Can't place a piece there, please try another move."

    def place_piece(self, color, column_number, row_index=0):
        column_index = column_number - 1
        if row_index > 5:
            print(self.invalid_placement())
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
