from .board import Board

class Turn:
    def __init__(self, board):
        self.board = board
        self.game_rows = (2, 4, 6, 8, 10, 12)

    def split_row(self, row):
        return row.split(' ')
