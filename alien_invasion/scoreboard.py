import pygame.font
from pygame.sprite import Group

from fighter import Fighter

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game):
        """Initialize scorekeeping attributes"""
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prep the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_fighters()

    def prep_score(self):
        """Turn the score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{self.stats.score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        # Display the score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, 
                                                self.settings.bg_color)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_fighters(self):
        """Show how many fighters are left"""
        self.fighters = Group()
        for fighter_num in range(self.stats.ships_left):
            fighter = Fighter(self.game)
            fighter.rect.x = 10 + fighter_num * fighter.rect.width
            fighter.rect.y = 10
            self.fighters.add(fighter)


    def check_high_score(self):
        """Check to see if this is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score and level to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.fighters.draw(self.screen)