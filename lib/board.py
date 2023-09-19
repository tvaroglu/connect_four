class Board:

    def __init__(self):
        '''
        all board coordinates:
           1.    2.    3.    4.    5.    6.    7.
        -------------------------------------------
        | 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 |
        -------------------------------------------
        | 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 |
        -------------------------------------------
        | 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 |
        -------------------------------------------
        | 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 |
        -------------------------------------------
        | 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 |
        -------------------------------------------
        | 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 |
        -------------------------------------------
        '''
        self.column_range = range(1, 8)
        self.default     = '  '
        self.red_piece   = '🟥'
        self.black_piece = '⬛️'
        # self.grid = [list(self.default * 6) for i in self.column_range]
        self.grid = [list(self.default * 3) for i in self.column_range]

    def eval(self):
        board_full = all([len([slot for slot in col \
                               if slot in (self.red_piece, self.black_piece)]) == 6 \
                                for col in self.grid])
        if board_full:
            return 'draw'
        eval = {
            'columns':   self.eval_columns(),
            'rows':      self.eval_rows(),
            'diagonals': self.eval_diagonals(),
        }
        results = [result for criteria, result in eval.items() if result]
        result = results[0] if len(results) > 0 else None
        return result

    def eval_diagonals(self):
        cols = len(self.grid)
        rows = max(len(col) for col in self.grid)
        red_wins, black_wins = False, False
        # Check diagonals starting from the top-left corner
        results = list()
        for col in range(cols):
            for row in range(rows):
                if row + 4 <= rows and col + 4 <= cols:
                    # Check the diagonal sequence from (col, row)
                    results = [self.grid[col + x][row + x] for x in range(4)]
                    red_wins   = self.red_piece * 4 in ''.join(results)
                    black_wins = self.black_piece * 4 in ''.join(results)
                    if red_wins:
                        return 'red'
                    if black_wins:
                        return 'black'
        # Check diagonals starting from the top-right corner
        results = list()
        for col in range(cols):
            for row in range(rows - 1, -1, -1):
                if row - 4 + 1 >= 0 and col + 4 <= cols:
                    # Check the diagonal sequence from (col, row)
                    results = [self.grid[col + x][row - x] for x in range(4)]
                    red_wins   = self.red_piece * 4 in ''.join(results)
                    black_wins = self.black_piece * 4 in ''.join(results)
                    if red_wins:
                        return 'red'
                    if black_wins:
                        return 'black'

    def eval_rows(self):
        for idx, col in enumerate(self.grid):
            row = [self.grid[sub_idx][idx] for sub_idx in range(0, len(self.grid)) \
                   if idx < len(self.grid[sub_idx]) - 1]
            red_wins   = self.red_piece * 4 in ''.join(row)
            black_wins = self.black_piece * 4 in ''.join(row)
            if red_wins:
                return 'red'
            if black_wins:
                return 'black'

    def eval_columns(self):
        for col in self.grid:
            red_wins   = self.red_piece * 4 in ''.join(col)
            black_wins = self.black_piece * 4 in ''.join(col)
            if red_wins:
                return 'red'
            if black_wins:
                return 'black'

    def place_piece(self, color, column_idx):
        try:
            valid_placement = len([slot for slot in self.grid[column_idx] \
                                if slot not in (self.red_piece, self.black_piece)]) > 0
        except IndexError:
            valid_placement = False
        if not valid_placement:
            return False
        for row_idx, slot in enumerate(self.grid[column_idx]):
            if slot not in (self.red_piece, self.black_piece):
                self.grid[column_idx][row_idx] = color
                return True

    def get_color(self, piece):
        result = self.default
        if piece == self.red_piece:
            result = 'red'
        if piece == self.black_piece:
            result = 'black'
        return result

    def get_piece(self, slot):
        result = self.default
        if slot == self.red_piece:
            result = self.red_piece
        if slot == self.black_piece:
            result = self.black_piece
        return result

    def print_row(self, row, row_idx):
        divider = '------' * 6
        print(''.join(row).replace('||', '|'))
        if row_idx == 6:
            result = ''
            for i in self.column_range:
                result += f'  {i}. '
            print(result)
        print(divider)

    def print_board(self, result=list(), row_idx=6):
        self.print_row(result, row_idx)
        if row_idx <= 0:
            return
        slot, result = '|    ', list()
        for col in self.grid:
            row = ''
            try:
                formatted = slot.replace(
                    '    ', f' {self.get_piece(col[row_idx - 1])} ')
            except IndexError:
                formatted = slot
            row += formatted
            result.append(f'{row}|')
        row_idx -= 1
        return self.print_board(result=result, row_idx=row_idx)
