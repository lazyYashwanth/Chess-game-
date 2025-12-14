import os
import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        base = os.path.join(os.path.dirname(__file__), "..", "assets", "sounds")
        self.move_sound = self._load(base, "move.wav")
        self.capture_sound = self._load(base, "capture.wav")

    def _load(self, base, name):
        path = os.path.join(base, name)
        if os.path.exists(path):
            return pygame.mixer.Sound(path)
        return None

    def play_move(self):
        if self.move_sound:
            self.move_sound.play()

    def play_capture(self):
        if self.capture_sound:
            self.capture_sound.play()
