# moduli pyGame
from pygame.sprite import Group
import pygame
import sys

# moduli progetto
from ship import Ship
import gameFunctions as gf
from setting import Settings
from game_stats import Game_stats
from button import Button
from scoreboard import  Scoreboard

def run_game():
    #inizilizziamo il gioco e creiamo gli oggetti a schermo
    pygame.init()
    #instanziamo un oggetto impostazioni
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #crazione istanza delle statistiche di gioco
    stats= Game_stats(ai_settings)

    # crazione bottone per avvio del gioco
    play_button= Button(ai_settings,screen,"Touch here or type 'p'")

    # creazione scoreboard
    scoreboard= Scoreboard(ai_settings,screen, stats)

    # creazione navetta
    ship = Ship(screen, ai_settings)

    # creazione  gruppo per alieni
    aliens = Group()

    # creazione della flotta di alieni
    gf.create_fleet(ai_settings,screen,aliens, ship)

    # gruppo dove immagazzinare i proiettili
    bullets = Group()


    #inzia il loop principale per il gioco
    while True:
        # rileva eventi di input
        gf.check_events(ai_settings, screen,stats, play_button, ship, bullets, aliens,scoreboard)

        if stats.game_active:
            # aggiorna posizione nave
            ship.update()
            # aggiorna posizione alieni
            gf.update_aliens(ai_settings, stats, screen, aliens, ship,bullets)
            # aggiorna posizione proiettili
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens, stats, scoreboard)

     #  else:
     #      sys.exit()

        # aggiorna oggetti a schermo
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, scoreboard)

run_game()