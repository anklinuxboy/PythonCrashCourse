import sys
from time import sleep
from button import Button

import pygame
from settings import Settings
from game_stats import GameStats
from fighter import Fighter
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.fighter = Fighter(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_aliens()

        # Start alien invasion in an active state
        self.game_active = False

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.fighter.update()
                self._update_bullets()
                self._update_aliens()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game settings
            self.settings.initialize_dynamic_settings()

            # Reset the game stats
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_fighters()
            self.game_active = True

            # Get rid of bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_aliens()
            self.fighter.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have collided
        # check for any bullets that have hit aliens
        # if so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_aliens()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _create_aliens(self):
        """Create the fleet of aliens"""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 8 * alien_height):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_pos, y_pos):
        """Create an alien and place it in row"""
        new_alien = Alien(self)
        new_alien.x = x_pos

        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.fighter.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_aliens(self):
        """Check if fleet at edge, update positions"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.fighter, self.aliens):
            print("Ship hit!")
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1
            self.sb.prep_fighters()

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.fighter.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()