import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):  # sottoclasse di Sprite, serve per poter creare un gruppo di proiettili
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen= screen

        #creiamo un proiettile a (0,0) e dopo gli impostiamo la corretta posizione
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top= ship.rect.top

        #salviamo il valore della posizione come un valore decimale
        self.y= float (self.rect.y)

        self.color= ai_settings.bullet_color
        self.speed_factor= ai_settings.bullet_speed_factor

    def update(self):
        # muovi i proiettili sullo schermo
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
       # pygame.display.update()

