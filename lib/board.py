class Board:
    def __init__(self):
        self.column_range = range(1, 8)
        self.row_range = range(1, 8)
        self.red_piece = '🟥'
        self.black_piece = '⬛️'

    def column_labels(self):
        output_list = []
        for i in self.column_range:
            output_list.append(f' {str(i)}.  ')
        return output_list

    def full_column_label(self):
        joined = ''.join(self.column_labels())
        return f' {joined}'

    def row_dividers(self):
        output_list = []
        section = '+----'
        for i in self.column_range:
            output_list.append(section)
        output_list[-1] = section + '+'
        return output_list

    def empty_row(self):
        output_list = []
        section = '|    '
        for i in self.column_range:
            output_list.append(section)
        output_list[-1] = section + '|'
        return output_list

    def construct_board(self):
        board = [self.full_column_label()]
        for row in self.row_range:
            board.append(self.row_dividers())
            board.append(self.empty_row())
        board.pop()
        return board
