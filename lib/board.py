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
        self.default    = ' '
        self.red_piece  = '🟥'
        self.blue_piece = '🟦'
        self.grid = [[self.default] * 6 for _ in self.column_range]

    def eval(self, seq_number=4, eval_color='red'):
        '''
        Public evaluation wrapper for rows, columns, and diagonals
        '''
        board_full = all(
            sum(slot in (self.red_piece, self.blue_piece) for slot in col) == 6
            for col in self.grid
        )
        if board_full: return 'draw'
        evaluators = {
            'columns':   self.eval_columns(seq_number),
            'rows':      self.eval_rows(seq_number),
            'diagonals': self.eval_diagonals(seq_number),
        }
        for _, result in evaluators.items():
            if result:
                if seq_number == 4:
                    return result[0]
                if seq_number == 3 and result[0] == eval_color:
                    return result[1]
        return None

    def eval_columns(self, seq_number=4):
        return self._scan_lines(kind='cols', seq_number=seq_number, win_index=True)

    def eval_rows(self, seq_number=4):
        return self._scan_lines(kind='rows', seq_number=seq_number, win_index=False)

    def eval_diagonals(self, seq_number=4):
        return self._scan_lines(kind='diags', seq_number=seq_number, win_index=False)

    def _get_piece(self, c, r):
        '''
        return token at (c, r) or self.default if beyond current fill
        '''
        return self.grid[c][r] if r < len(self.grid[c]) else self.default

    def _is_valid_drop(self, c, r):
        '''
        valid only if r equals current filled height of column c
        '''
        filled = sum(1 for slot in self.grid[c] if slot in (self.red_piece, self.blue_piece))
        return r == filled

    def _lines(self, kind):
        '''
        Yield lists of (c, r) indices: rows, columns, or diagonals. Only lines with length >= 4.
        '''
        cols, rows = 7, 6
        if kind in ('rows', 'all'):
            for r in range(rows):
                yield [(c, r) for c in range(cols)]
        if kind in ('cols', 'all'):
            for c in range(cols):
                yield [(c, r) for r in range(rows)]
        if kind in ('diags', 'all'):
            # bottom-left -> top-right:
            for c0 in range(cols):
                diag = []
                c, r = c0, 0
                while 0 <= c < cols and 0 <= r < rows:
                    diag.append((c, r)); c += 1; r += 1
                if len(diag) >= 4:
                    yield diag
            for r0 in range(1, rows):
                diag = []
                c, r = 0, r0
                while 0 <= c < cols and 0 <= r < rows:
                    diag.append((c, r)); c += 1; r += 1
                if len(diag) >= 4:
                    yield diag
            # top-left -> bottom-right:
            for c0 in range(cols):
                diag = []
                c, r = c0, rows - 1
                while 0 <= c < cols and 0 <= r < rows:
                    diag.append((c, r)); c += 1; r -= 1
                if len(diag) >= 4:
                    yield diag
            for r0 in range(rows - 2, -1, -1):
                diag = []
                c, r = 0, r0
                while 0 <= c < cols and 0 <= r < rows:
                    diag.append((c, r)); c += 1; r -= 1
                if len(diag) >= 4:
                    yield diag

    def _scan_lines(self, kind, seq_number, win_index=False):
        '''
        Scan the given line kind using 4-length sliding windows.
        Returns:
          - (color, col_idx) on 4-in-a-row win if win_index=True (columns)
          - (color, None)   on 4-in-a-row win if win_index=False (rows/diags)
          - (color, col_idx) on 3+empty where empty is a valid drop
          - None otherwise
        '''
        red, bl = self.red_piece, self.blue_piece
        for indices in self._lines(kind):
            # slide a 4-wide window over this line:
            for start in range(0, len(indices) - 4 + 1):
                window_idx = indices[start:start + 4]
                pieces = [self._get_piece(c, r) for c, r in window_idx]
                if seq_number == 4:
                    if pieces == [red]*4:
                        payload = window_idx[0][0] if win_index else None
                        return ('red', payload)
                    if pieces == [bl]*4:
                        payload = window_idx[0][0] if win_index else None
                        return ('blue', payload)
                elif seq_number == 3:
                    for color, token in (('red', red), ('blue', bl)):
                        if pieces.count(token) == 3 and pieces.count(self.default) == 1:
                            i = pieces.index(self.default)
                            c, r = window_idx[i]
                            if self._is_valid_drop(c, r):
                                return (color, c)
        return None

    def place_piece(self, color, column_idx):
        if not (0 <= column_idx < 7): return False
        col = self.grid[column_idx]
        for i in range(len(col)):
            if col[i] not in (self.red_piece, self.blue_piece):
                self.grid[column_idx][i] = color
                return True
        return False

    def get_color(self, piece):
        if piece == self.red_piece: return 'red'
        if piece == self.blue_piece: return 'blue'
        return self.default

    def get_piece(self, slot):
        return slot if slot in (self.red_piece, self.blue_piece) else self.default

    def render_row(self, row, row_idx):
        divider = '------' * 6
        print(''.join(row).replace('||', '|'))
        if row_idx == 6:
            print(''.join([f'  {i}. ' for i in self.column_range]))
        print(divider)

    def render_board(self, result=[], row_idx=6):
        self.render_row(result, row_idx)
        if row_idx <= 0: return
        new_row = []
        for col in self.grid:
            try:
                slot = self.get_piece(col[row_idx - 1])
            except IndexError:
                slot = self.default
            if slot == self.default:
                piece = '    '       # 4 spaces for an empty cell
            else:
                piece = f' {slot} '  # center the emoji in 4 spaces
            new_row.append(f'|{piece}|')
        return self.render_board(result=new_row, row_idx=row_idx - 1)
