import sys
import pygame

def check_events(ship):
    # attendi un evento di input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT è un tipo di evento
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # muovi la nave a destra
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # muovi la nave a sinistra
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # ferma il movimento  della nave a destra
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                # muovi la nave a sinistra
                ship.moving_left = False


def update_screen(ai_settings, screen,ship):

    screen.fill(ai_settings.bg_color)     #  per colorare lo sfondo
    ship.draw_me()
    # rendi lo schermo con gli oggetti più recenti visibile, aggiorna lo schermo
    pygame.display.flip()
