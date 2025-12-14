import pygame
from .const import SQSIZE


class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_mouse(self, pos):
        self.mouse_x, self.mouse_y = pos

    def save_initial(self, pos):
        self.initial_col = pos[0] // SQSIZE
        self.initial_row = pos[1] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def get_square_under_mouse(self):
        return self.mouse_y // SQSIZE, self.mouse_x // SQSIZE

    def update_blit(self, surface):
        if not self.dragging or not self.piece:
            return
        img = self.piece.get_surface(SQSIZE)
        x = self.mouse_x - SQSIZE // 2
        y = self.mouse_y - SQSIZE // 2
        if img:
            surface.blit(img, (x, y))
        else:
            # fallback circle if images are missing
            pygame.draw.circle(surface, (200, 200, 200), (self.mouse_x, self.mouse_y), SQSIZE // 2)
