import pygame
from pygame.sprite import Sprite

class Fighter(Sprite):
    """Class to manage the fighter"""

    def __init__(self, game):
        """Initialize the fighter bitmap"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update this ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fighter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fighter_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship"""       
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)