import sys

import pygame
from settings import Settings
from fighter import Fighter
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.fighter = Fighter(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.fighter.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.fighter.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.fighter.moving_left = True
                    elif event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.fighter.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.fighter.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets"""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.fighter.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()