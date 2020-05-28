import sys
import pygame
from bullet import Bullet


def fire_bullets(ai_settings,screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:  #
        print("sparo")
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # muovi la nave a destra
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # muovi la nave a sinistra
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # ferma il movimento  della nave a destra
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # muovi la nave a sinistra
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # attendi un evento di input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT è un tipo di evento
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_bullets(bullets):
    bullets.update()
    # cancellare i proiettili fuori dallo schermo
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen,ship, bullets):

    #disegna tutti i proiettili dietro la nave e gli aleni
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    screen.fill(ai_settings.bg_color)     #  per colorare lo sfondo
    ship.draw_me()
    # rendi lo schermo con gli oggetti più recenti visibile, aggiorna lo schermo
    pygame.display.update()
