import pygame
from .board import Board
from .config import Config
from .const import ROWS, COLS, SQSIZE
from .dragger import Dragger
from .sound import Sound


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()
        self.sound = Sound()
        self.turn = "white"

    def reset(self):
        self.__init__()

    def next_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

    def show_bg(self, surface):
        light, dark = self.config.theme.square_colors()
        for row in range(ROWS):
            for col in range(COLS):
                color = light if (row + col) % 2 == 0 else dark
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for sq in (initial, final):
                highlight = pygame.Surface((SQSIZE, SQSIZE), pygame.SRCALPHA)
                highlight.fill((*self.config.theme.highlight, 90))
                surface.blit(highlight, (sq.col * SQSIZE, sq.row * SQSIZE))

    def show_moves(self, surface):
        if not self.dragger.dragging or not self.dragger.piece:
            return
        for move in self.dragger.piece.moves:
            row, col = move.final.row, move.final.col
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(surface, self.config.theme.hint, center, 10)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.squares[row][col].piece
                if piece is None:
                    continue
                if self.dragger.dragging and piece == self.dragger.piece:
                    continue
                sprite = piece.get_surface(SQSIZE)
                if sprite:
                    x = col * SQSIZE + (SQSIZE - sprite.get_width()) // 2
                    y = row * SQSIZE + (SQSIZE - sprite.get_height()) // 2
                    surface.blit(sprite, (x, y))
                else:
                    # fallback circle if image missing
                    pygame.draw.circle(surface, self.config.theme.drag, (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2), SQSIZE // 2 - 6, 3)

    def show_dragged(self, surface):
        self.dragger.update_blit(surface)

    def play_sound(self, captured):
        if captured:
            self.sound.play_capture()
        else:
            self.sound.play_move()
