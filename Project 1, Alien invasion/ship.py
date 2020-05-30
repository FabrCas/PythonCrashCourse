import pygame
from pygame.sprite import  Sprite

class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        super().__init__()
        #la posizione della navetta sullo schermo, parametro -> display object
        self.screen= screen
        self.ai_settings= ai_settings
        self.is_alive = True
        self.is_flipped = False


        # carica l'immagine della navetta e ottieni la sua rect
        self.image= pygame.image.load("static/images/spaceship.png")
        self.image= pygame.transform.scale(self.image, (70, 70)) # for space ship
        # self.image = pygame.transform.scale(self.image, (90, 110))

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
        self.do_rotation180 = False
        self.is_rotated = False

        # posizioniamo la navetta
        self.rect.centerx= self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom #- (self.rect.width/2)

    def update(self):
        # print("up: " + str(self.moving_forward) + " down: "+ str(self.moving_back) + " left: " + str(self.moving_left) + " right: " + str(self.moving_right) )
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_forward  and self.rect.top > 150:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_back and self.rect.bottom < self.screen_rect.height:
            self.bottom += self.ai_settings.ship_speed_factor
        if self.do_rotation180:
            self.center = self.rect.center
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect =self.image.get_rect(center= self.center)
            self.do_rotation180 = False
            if self.is_flipped:
                self.is_flipped = False
            else:
                self.is_flipped = True



        self.rect.centerx = self.centerx #solo la parte intera di self.center verrà assegnata alla rect
        self.rect.bottom = self.bottom

   # def rot_center(image, angle):
#
   #     center = image.get_rect().center
   #     rotated_image = pygame.transform.rotate(image, angle)
   #     new_rect = rotated_image.get_rect(center=center)
#
   #     return rotated_image, new_rect


    def draw_me(self):
            self.screen.blit(self.image, self.rect)
           # pygame.display.update()

    #posiziona la nave al centro (punto di partenza)
    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        self.is_alive = True
        if self.is_flipped:
            self.is_flipped = False
            self.center = self.rect.center
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(center=self.center)


    def reset_flag(self):
        self.moving_back = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_right = False
        self.do_rotation180 = False
