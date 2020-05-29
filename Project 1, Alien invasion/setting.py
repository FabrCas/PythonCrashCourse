class Settings():
    def __init__(self):
        # setteggi schermo
        self.screen_width= 1200
        self.screen_height= 900
        self.bg_color = (230,230,230)
        self.ship_limit = 3

        # valori per i proiettili
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (128,0,0)
        self.bullet_allowed = 3

        # settaggi per gli alieni
        self.fleet_drop_speed = 10

        # speed up del gioco
        self.speedup_scale = 1.1

        # variabile utilizzata per indicare che al momento non è stato ucciso nessun alieno
        self.aliens_alive = -1

        # variabili score
        self.score_scale = 1.5
        #metodi costruttore
        self.initillize_dynamic_settings()



    def initillize_dynamic_settings(self):
        # velocità della nave
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        # 1 -> destra, -1 -> sinistra
        self.fleet_direction = 1

        # scoring
        self.alien_points= 50

    def increase_speed(self):
        self.ship_speed_factor   *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor  *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


