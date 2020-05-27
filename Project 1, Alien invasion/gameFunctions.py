import sys
import pygame


def check_events(ship):
    # attendi un evento di input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT è un tipo di evento
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                #muovi la nave a destra
                ship.rect.centerx += 1

def update_screen(ai_settings, screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.draw_me()
    # rendi lo schermo con gli oggetti più recenti visibile, aggiorna lo schermo
    pygame.display.flip()
