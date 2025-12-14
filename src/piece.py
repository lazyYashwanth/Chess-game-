import os
import pygame


class Piece:
    def __init__(self, name, color):
        self.name = name  # pawn, knight, bishop, rook, queen, king
        self.color = color  # white or black
        self.moved = False
        self.dir = -1 if color == "white" else 1
        self.texture_path = None
        self._surface = None
        self._cached_size = None
        self.set_texture(size=80)
        self.moves = []

    def set_texture(self, size=80):
        base = os.path.join(os.path.dirname(__file__), "..", "assets", "images", f"imgs-{size}px")
        self.texture_path = os.path.join(base, f"{self.color}_{self.name}.png")
        self._cached_size = None
        self._surface = None

    def get_surface(self, size):
        # Only use cache if same size
        if self._surface is not None and self._cached_size == size:
            return self._surface
        
        if self.texture_path and os.path.exists(self.texture_path):
            try:
                image = pygame.image.load(self.texture_path).convert_alpha()
                self._surface = pygame.transform.smoothscale(image, (size, size))
                self._cached_size = size
                return self._surface
            except Exception as e:
                print(f"Error loading {self.texture_path}: {e}")
                return None
        return None

    def add_moves(self, moves):
        self.moves = moves

    def clear_moves(self):
        self.moves = []

    def __repr__(self):
        return f"{self.color} {self.name}"
