from .const import ROWS, COLS
from .square import Square
from .piece import Piece
from .move import Move


class Board:
    def __init__(self):
        self.squares = [[Square(r, c) for c in range(COLS)] for r in range(ROWS)]
        self.last_move = None
        self._create()

    def _create(self):
        for col in range(COLS):
            self._add_piece(Piece("pawn", "white"), 6, col)
            self._add_piece(Piece("pawn", "black"), 1, col)

        placements = [
            ("rook", 0),
            ("knight", 1),
            ("bishop", 2),
            ("queen", 3),
            ("king", 4),
            ("bishop", 5),
            ("knight", 6),
            ("rook", 7),
        ]
        for name, col in placements:
            self._add_piece(Piece(name, "white"), 7, col)
            self._add_piece(Piece(name, "black"), 0, col)

    def _add_piece(self, piece, row, col):
        self.squares[row][col].piece = piece

    def move(self, piece, move):
        start_sq = self.squares[move.initial.row][move.initial.col]
        end_sq = self.squares[move.final.row][move.final.col]
        captured = end_sq.piece
        end_sq.piece = piece
        start_sq.piece = None
        piece.moved = True
        self.last_move = move
        return captured

    def piece_at(self, row, col):
        if not Square.in_range(row, col):
            return None
        return self.squares[row][col].piece

    def valid_moves(self, piece, row, col):
        moves = []
        name = piece.name
        if name == "pawn":
            moves += self._pawn_moves(piece, row, col)
        elif name == "knight":
            moves += self._knight_moves(piece, row, col)
        elif name == "bishop":
            moves += self._slide_moves(piece, row, col, [(-1, -1), (-1, 1), (1, -1), (1, 1)])
        elif name == "rook":
            moves += self._slide_moves(piece, row, col, [(-1, 0), (1, 0), (0, -1), (0, 1)])
        elif name == "queen":
            moves += self._slide_moves(
                piece,
                row,
                col,
                [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
            )
        elif name == "king":
            moves += self._king_moves(piece, row, col)
        return moves

    def _pawn_moves(self, piece, row, col):
        moves = []
        step = piece.dir
        start_row = 6 if piece.color == "white" else 1
        one_ahead = row + step
        if Square.in_range(one_ahead, col) and self.squares[one_ahead][col].is_empty():
            moves.append(Move(Square(row, col), Square(one_ahead, col)))
            two_ahead = row + 2 * step
            if row == start_row and self.squares[two_ahead][col].is_empty():
                moves.append(Move(Square(row, col), Square(two_ahead, col)))
        for dc in (-1, 1):
            r, c = row + step, col + dc
            if Square.in_range(r, c) and self.squares[r][c].has_enemy_piece(piece.color):
                moves.append(Move(Square(row, col), Square(r, c)))
        return moves

    def _knight_moves(self, piece, row, col):
        moves = []
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            r, c = row + dr, col + dc
            if not Square.in_range(r, c):
                continue
            target = self.squares[r][c]
            if target.is_empty() or target.has_enemy_piece(piece.color):
                moves.append(Move(Square(row, col), Square(r, c)))
        return moves

    def _king_moves(self, piece, row, col):
        moves = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if not Square.in_range(r, c):
                    continue
                target = self.squares[r][c]
                if target.is_empty() or target.has_enemy_piece(piece.color):
                    moves.append(Move(Square(row, col), Square(r, c)))
        return moves

    def _slide_moves(self, piece, row, col, directions):
        moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while Square.in_range(r, c):
                target = self.squares[r][c]
                if target.is_empty():
                    moves.append(Move(Square(row, col), Square(r, c)))
                elif target.has_enemy_piece(piece.color):
                    moves.append(Move(Square(row, col), Square(r, c)))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves
