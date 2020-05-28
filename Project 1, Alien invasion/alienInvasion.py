# moduli pyGame
from pygame.sprite import Group
import pygame

# moduli progetto
from ship import Ship
from alien import Alien
import gameFunctions as gf
from setting import Settings

def run_game():
    #inizilizziamo il gioco e creiamo gli oggetti a schermo
    pygame.init()
    #instanziamo un oggetto impostazioni
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")


    # creazione navetta
    ship = Ship(screen, ai_settings)

    # creazione alieno/i
    alien = Alien(screen, ai_settings)

    # gruppo dove immagazzinare i proiettili
    bullets = Group()


    #inzia il loop principale per il gioco
    while True:
        # rileva eventi di input
        gf.check_events(ai_settings, screen, ship, bullets)
        # aggiorna posizione nave
        ship.update()
        # aggiorna posizione proiettili
        gf.update_bullets(bullets)
        # aggiorna oggetti a schermo
        gf.update_screen(ai_settings, screen, ship,alien, bullets)


run_game()