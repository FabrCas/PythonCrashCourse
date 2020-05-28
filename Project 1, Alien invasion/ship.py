import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        #la posizione della navetta sullo schermo, parametro -> display object
        self.screen= screen
        self.ai_settings= ai_settings

        # carica l'immagine della navetta e ottieni la sua rect
        self.image= pygame.image.load("./static/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()

        self.center = float(self.screen_rect.centerx)


        # flag per il movimento a destra
        self.moving_right= False
        # flag per il movimento a sinistra
        self.moving_left = False

        # posizioniamo la navetta
        self.rect.centerx= self.screen_rect.centerx

        self.rect.bottom= self.screen_rect.bottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


        self.rect.centerx= self.center #solo la parte intera di self.center verrà assegnata alla rect

    def draw_me(self):
            self.screen.blit(self.image, self.rect)
           # pygame.display.update()


