import pygame
from pygame.sprite import Sprite

class Alien (Sprite):

    def __init__(self,screen, ai_settings):
        super().__init__()
        self.screen= screen
        self.ai_settings = ai_settings

        #caricamento dell'immagine
        self.image = pygame.image.load("./static/images/alien.bmp")
        self.rect = self.image.get_rect()

        #l'alieno "spawna" vicino l'angolo in alto a sinistra
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #salviamo la posizione effettiva dell'alieno
        self.x = float(self.rect.x)

    def draw_me(self):
        self.screen.blit(self.image,self.rect)

