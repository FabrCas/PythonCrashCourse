import gameFunctions as gf
from setting import Settings
from pygame.sprite import Group
import pygame

from ship import Ship

def run_game():
    #inizilizziamo il gioco e creiamo gli oggetti a schermo
    pygame.init()
    #instanziamo un oggetto impostazioni
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")


    #creazione navetta
    ship = Ship(screen, ai_settings)

    # gruppo dove immagazzinare i proiettili
    bullets= Group()


    #inzia il loop principale per il gioco
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()