class GameStats:
    """Track stats for alien invasion"""

    def __init__(self, game):
        """Initialize stats"""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats that can change"""
        self.ships_left = self.settings.ship_limit