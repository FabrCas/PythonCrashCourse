import sys
import pygame

from alien import Alien
from bullet import Bullet

#start-------------------------aliens---------------------------------------

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings,aliens)
            break # basta controllare che un alieno superi i limiti di schermo

def change_fleet_direction(ai_settings,aliens):
    #cambio la direzione per tutti gli alieni e li faccio scendere
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    #controllo se la flotta ha raggiunto il limite dello schermo
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y= ai_settings.screen_height - ship_height - (alien_height*3)
    number_rows= int(available_space_y/(alien_height*2))
    print(alien_height)
    print(number_rows)
    return  number_rows

def get_number_of_alines(ai_settings, alien_width):
    # code for finding the number of aliens which we have to generate
    available_space_x = ai_settings.screen_width - (alien_width * 2)
    return int(available_space_x / (alien_width * 2))

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien_width= alien.rect.width
    alien_height= alien.rect.height
    alien.x = alien.x + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.y + 2* alien_height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens, ship):
    alien = Alien(screen,ai_settings)  # istanza della classe Alieno utile per avere info sulla larghezza della rect
    number_aliens_x = get_number_of_alines(ai_settings, alien.rect.width)
    number_rows= get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    #creiamo gli alieni
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number, row_number)

#end-------------------------aliens---------------------------------------

#start-------------------------shooting-------------------------------------
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
    elif event.key == pygame.K_q:    #uscita dal gioco premendo 'q'
        sys.exit()


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
    print(len(bullets))

#end-------------------------shooting-------------------------------------

def update_screen(ai_settings, screen,ship, aliens ,bullets):

    screen.fill(ai_settings.bg_color)  # per colorare lo sfondo
    #disegna tutti i proiettili dietro la nave e gli aleni
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #disegna gli alieni, si e' usato un modo diverso per fare la stessa cosa fatta per i proiettili nelle righe sopra
    aliens.draw(screen)
    ship.draw_me()
    # rendi lo schermo con gli oggetti più recenti visibile, aggiorna lo schermo
    pygame.display.update()
