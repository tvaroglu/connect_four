class Board:
    def __init__(self):
        self.column_range = range(1, 8)
        self.row_range = range(1, 8)

    def column_labels(self):
        output_list = []
        for i in self.column_range:
            output_list.append(f' {str(i)}  ')
        return output_list

    def full_column_label(self):
        joined = ''.join(self.column_labels())
        return f' {joined}'

    def row_dividers(self):
        output_list = []
        section = '+---'
        for i in self.column_range:
            output_list.append(section)
        output_list[-1] = section + '+'
        return output_list

    def full_row_divider(self):
        return ''.join(self.row_dividers())

    def board_setup(self):
        board = [self.full_column_label()]
        for row in self.row_range:
            board.append(self.full_row_divider())
        return board

    def print_board(self):
        for row in self.board_setup():
            print(row)


# b = Board()
# b.print_board()
