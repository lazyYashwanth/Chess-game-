class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece is not None

    def is_empty(self):
        return self.piece is None

    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color

    @staticmethod
    def in_range(*values):
        return all(0 <= v <= 7 for v in values)

    def __eq__(self, other):
        return isinstance(other, Square) and self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"({self.row},{self.col})"
