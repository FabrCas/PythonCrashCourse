import pygame
from pygame.sprite import  Sprite

class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        super().__init__()
        #la posizione della navetta sullo schermo, parametro -> display object
        self.screen= screen
        self.ai_settings= ai_settings


        # carica l'immagine della navetta e ottieni la sua rect
        self.image= pygame.image.load("static/images/ship.bmp")
        #self.image= pygame.transform.scale(self.image, (20, 40))

        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()

        self.centerx = float(self.screen_rect.centerx)
        self.bottom = self.screen_rect.bottom


        # flag per il movimento a destra
        self.moving_right= False
        # flag per il movimento a sinistra
        self.moving_left = False
        # flag per il movimento in avanti
        self.moving_forward = False
        # flag per il movimento indietro
        self.moving_back = False
        # flag per cambiare direzione
        self.is_rotated180 = False

        # posizioniamo la navetta
        self.rect.centerx= self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom #- (self.rect.width/2)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_forward  and self.rect.top > 150:
            print("muovo su")
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_back and self.rect.bottom < self.screen_rect.height:
            print("muovo giù")
            self.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx #solo la parte intera di self.center verrà assegnata alla rect
        self.rect.bottom = self.bottom

    def draw_me(self):
            self.screen.blit(self.image, self.rect)
           # pygame.display.update()

    #posiziona la nave al centro (punto di partenza)
    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom


