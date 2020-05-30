import pygame
from pygame.sprite import Sprite

class Alien (Sprite):

    def __init__(self,screen, ai_settings):
        super().__init__()
        self.screen= screen
        self.ai_settings = ai_settings

        #caricamento dell'immagine
        self.image = pygame.image.load("./static/images/alien2.png")
        self.image = pygame.transform.scale(self.image, (80, 80))  # for alien
        self.rect = self.image.get_rect()

        #l'alieno "spawna" vicino l'angolo in alto a sinistra
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #salviamo la posizione effettiva dell'alieno
        self.x = float(self.rect.x)

    def draw_me(self):
        self.screen.blit(self.image,self.rect)
     #   pygame.display.update()

    def check_edge(self):
        screen_rect= self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

