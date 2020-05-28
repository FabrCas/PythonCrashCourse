class Settings():
    def __init__(self):
        # setteggi schermo
        self.screen_width= 1200
        self.screen_height= 800
        self.bg_color = (230,230,230)
        # velocità della nave
        self.ship_speed_factor =  1.5
        # valori per i proiettili
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (128,0,0)
        self.bullet_allowed = 3
        # settaggi per gli alieni
        self.alien_speed_factor = 1
        # 1 -> destra, -1 -> sinistra
        self.fleet_direction = 1
        self.fleet_drop_speed= 10

