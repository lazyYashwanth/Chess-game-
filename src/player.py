import pygame

class player:
    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.Surface((55, 55))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.speed = 7

    def ypdate(self, key_pressed):
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.rect += self.speed
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            self.rect.y -= self.speed
        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            self.rect += self.speed

    def fraw(self, screen):
        screen.blit(self.image, self.rect)
