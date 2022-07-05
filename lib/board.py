class Board:
    def __init__(self):
        self.column_range = range(1, 8)
        self.row_range = range(1, 8)
        self.red_piece = '🟥'
        self.black_piece = '⬛️'

    def column_labels(self):
        output_list = [f' {str(i)}.  ' for i in self.column_range]
        return output_list

    def full_column_label(self):
        joined = ''.join(self.column_labels())
        return f' {joined}'

    def row_dividers(self):
        section, final_section = '+----', '+----+'
        output_list = [section for i in self.column_range]
        output_list[-1] = final_section
        return output_list

    def empty_row(self):
        section, final_section = '|    ', '|    |'
        output_list = [section for i in self.column_range]
        output_list[-1] = final_section
        return output_list

    def construct_board(self):
        board = [self.full_column_label()]
        for row in self.row_range:
            board.append(self.row_dividers())
            board.append(self.empty_row())
        board.pop()
        return board
