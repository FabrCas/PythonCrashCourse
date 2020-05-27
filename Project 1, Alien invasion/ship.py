import pygame

class Ship():

    def __init__(self, screen):
        #la posizione della navetta sullo schermo, parametro -> display object
        self.screen= screen

        # carica l'immagine della navetta e ottieni la sua rect
        self.image= pygame.image.load("./static/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()

        # posizioniamo la navetta
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom

    def draw_me(self):
            self.screen.blit(self.image, self.rect)

