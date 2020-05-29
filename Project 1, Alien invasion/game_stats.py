class Game_stats():
    def __init__(self, ai_settings):
        self.ai_settings= ai_settings
        self.reset_stats()

        # inizialmente il gioco e' inattivo (menu)
        self.game_active = False

    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit