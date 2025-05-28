class Board:

    def __init__(self) -> None:
        '''
                            All board coords:

        |-------------------------------------------------------|
        | (0,5) | (1,5) | (2,5) | (3,5) | (4,5) | (5,5) | (6,5) |
        |-------------------------------------------------------|
        | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) | (5,4) | (6,4) |
        |-------------------------------------------------------|
        | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) | (5,3) | (6,3) |
        |-------------------------------------------------------|
        | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) | (5,2) | (6,2) |
        |-------------------------------------------------------|
        | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) | (5,1) | (6,1) |
        |-------------------------------------------------------|
        | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) | (5,0) | (6,0) |
        |-------------------------------------------------------|
        '''
        self.column_range = range(1, 8)
        self.default     = '  '
        self.red_piece   = '🟥'
        self.blue_piece  = '🟦'
        self.grid = [list(self.default * 3) for i in self.column_range]

    def eval(self, seq_number=4, eval_color='red'):
        board_full = all([len([slot for slot in col \
                               if slot in (self.red_piece, self.blue_piece)]) == 6 \
                                for col in self.grid])
        if board_full: return 'draw'
        eval = {
            'columns':   self.eval_columns(seq_number=seq_number),
            'rows':      self.eval_rows(seq_number=seq_number),
            'diagonals': self.eval_diagonals(seq_number=seq_number) \
                if seq_number == 4 else None,
        }
        results = [(criteria, result) for criteria, result in eval.items() if result]
        result = results[0][1] if len(results) > 0 else None
        # 2-player mode; return winning color to determine winner:
        if result and seq_number == 4: result = result[0]
        # Skynet turn (1-player mode); return col idx to block the other player's win:
        if result and seq_number == 3: result = result[1] \
            if result[0] == eval_color else None
        return result

    def eval_diagonals(self, seq_number=4):
        result_red = result_bl = False
        red, bl = self.red_piece, self.blue_piece
        cols = len(self.grid)
        rows = max(len(col) for col in self.grid)
        # Check diagonals starting from the top-left corner:
        results = []
        for col in range(cols):
            for row in range(rows):
                if row + seq_number <= rows and col + seq_number <= cols:
                    # Check the diagonal sequence from (col, row)
                    results = [self.grid[col + x][row + x] for x in range(seq_number)]
                    sequence = ''.join(results)
                    result_red = red * seq_number in sequence
                    result_bl = bl * seq_number in sequence
                    if result_red: return 'red', None
                    if result_bl: return 'blue', None
        # Check diagonals starting from the top-right corner:
        results = []
        for col in range(cols):
            for row in range(rows - 1, -1, -1):
                if row - seq_number + 1 >= 0 and col + seq_number <= cols:
                    # Check the diagonal sequence from (col, row)
                    results = [self.grid[col + x][row - x] for x in range(seq_number)]
                    sequence = ''.join(results)
                    result_red = red * seq_number in sequence
                    result_bl = bl * seq_number in sequence
                    if result_red: return 'red', None
                    if result_bl: return 'blue', None

    def eval_rows(self, seq_number=4):
        result_red = result_bl = False
        red, bl = self.red_piece, self.blue_piece
        for idx, col in enumerate(self.grid):
            row = [self.grid[sub_idx][idx] for sub_idx in range(0, len(self.grid)) \
                   if idx < len(self.grid[sub_idx]) - 1]
            sequence, block_idx = ''.join(row), 0
            if seq_number == 3:
                if red * seq_number + ' ' in sequence:
                    target = f'{self.red_piece} '
                    result_red, block_idx = True, sequence.index(target)
                if ' ' + red * seq_number in sequence:
                    target = f' {self.red_piece}'
                    result_red, block_idx = True, sequence.index(target)
                if bl * seq_number + ' ' in sequence:
                    target = f'{self.blue_piece} '
                    result_bl, block_idx = True, sequence.index(target)
                if ' ' + bl * seq_number in sequence:
                    target = f' {self.blue_piece}'
                    result_bl, block_idx = True, sequence.index(target)
            else:
                result_red = red * seq_number in sequence
                result_bl = bl * seq_number in sequence
            try:
                if result_red:
                    # import pdb; pdb.set_trace()
                    return 'red', row.index(' ', block_idx) if ' ' in row else None
                if result_bl:
                    return 'blue', row.index(' ', block_idx) if ' ' in row else None
            except ValueError:
                seq_number = seq_number + 1 if 1 <= seq_number < 7 else seq_number - 1
                return self.eval_rows(seq_number=seq_number)

    def eval_columns(self, seq_number=4):
        result_red = result_bl = False
        red, bl = self.red_piece, self.blue_piece
        for idx, col in enumerate(self.grid):
            sequence = ''.join(col)
            if seq_number == 3:
                result_red = red * seq_number + ' ' in sequence
                result_bl = bl * seq_number + ' ' in sequence
            else:
                result_red = red * seq_number in sequence
                result_bl = bl * seq_number in sequence
            if result_red: return 'red', idx
            if result_bl: return 'blue', idx

    def place_piece(self, color, column_idx):
        try:
            valid_placement = len([slot for slot in self.grid[column_idx] \
                                if slot not in (self.red_piece, self.blue_piece)]) > 0
        except IndexError:
            valid_placement = False
        if not valid_placement: return False
        for row_idx, slot in enumerate(self.grid[column_idx]):
            if slot not in (self.red_piece, self.blue_piece):
                self.grid[column_idx][row_idx] = color
                return True

    def get_color(self, piece):
        result = self.default
        if piece == self.red_piece: result = 'red'
        if piece == self.blue_piece: result = 'blue'
        return result

    def get_piece(self, slot):
        result = self.default
        if slot == self.red_piece: result = self.red_piece
        if slot == self.blue_piece: result = self.blue_piece
        return result

    def render_row(self, row, row_idx):
        divider = '------' * 6
        print(''.join(row).replace('||', '|'))
        if row_idx == 6:
            result = ''
            for i in self.column_range: result += f'  {i}. '
            print(result)
        print(divider)

    def render_board(self, result=[], row_idx=6):
        self.render_row(result, row_idx)
        if row_idx <= 0: return
        slot, result = '|    ', []
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
        return self.render_board(result=result, row_idx=row_idx)
