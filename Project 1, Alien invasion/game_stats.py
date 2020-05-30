class Game_stats():
    def __init__(self, ai_settings):
        self.ai_settings= ai_settings
        self.reset_stats()
        self.get_high_score()


        # inizialmente il gioco e' inattivo (menu)
        self.game_active = False

    def get_high_score(self):
        try:
            with open("highScore.txt", "r+") as self.fileHG:
                content = self.fileHG.readline()
                print(content)
                if content == "" or content == str(0):
                    print("il file highScore.txt non ha dati")
                    self.high_score = 0
                    self.fileHG.write(str(self.high_score))
                else:
                    self.high_score = float(content)
            self.fileHG.close()
        except FileNotFoundError:
            print("file highScore.txt non trovato")
            self.high_score = 0

    def write_high_score(self):
        try:
            with open("highScore.txt", "w") as self.fileHG:
                self.fileHG.write(str(self.score))
                self.fileHG.close()
        except FileNotFoundError:
            print("file highScore.txt non trovato")
        self.high_score = self.score



    def reset_stats(self):
        self.ships_left= self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

