import gameFunctions as gf
from setting import Settings
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


    #inzia il loop principale per il gioco
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()