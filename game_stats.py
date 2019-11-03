class GameStats():
    """Tracks statistics for Alien Invasion"""
    def __init__(self, ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in an inactive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initial statistics that can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0