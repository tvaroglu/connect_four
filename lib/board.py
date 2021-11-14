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
        joined = self.join_row(self.column_labels())
        return f' {joined}'

    def row_dividers(self):
        output_list = []
        section = '+---'
        for i in self.column_range:
            output_list.append(section)
        output_list[-1] = section + '+'
        return output_list

    def full_row_divider(self):
        return self.join_row(self.row_dividers())

    def empty_row(self):
        output_list = []
        section = '|   '
        for i in self.column_range:
            output_list.append(section)
        output_list[-1] = section + '|'
        return output_list

    def join_row(self, row):
        return ''.join(row)

    def construct_board(self, printable=False):
        board = [self.full_column_label()]
        for row in self.row_range:
            if printable:
                board.append(self.full_row_divider())
                board.append(self.join_row(self.empty_row()))
            else:
                board.append(self.row_dividers())
                board.append(self.empty_row())
        board.pop()
        return board

    def print_board(self):
        for row in self.construct_board(printable=True):
            print(row)
