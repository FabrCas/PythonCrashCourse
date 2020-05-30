import sys
import pygame
from pygame import  mixer
from time import sleep

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

def ship_hit(ai_settings, stats, screen,aliens, ship, bullets, scoreboard):
    ship.is_alive = False
    ship_hit_sound= mixer.Sound("static/sounds/shipHit.wav")
    ship_hit_sound.set_volume(1.0)
    ship_hit_sound.play()
    check_high_score(stats, scoreboard)
    pygame.event.clear()
    if stats.ships_left > 0:
        sleep(1.0)
        ship.reset_flag()
        stats.ships_left -= 1
        # distruggi oggetti
        aliens.empty()
        bullets.empty()
        # ricrea
        ship.center_ship()
        scoreboard.prep_ships() # aggiornare il numero di navi rimaste
        pygame.display.update()
        create_fleet(ai_settings, screen, aliens, ship)
    else:
        stats.game_active= False
        pygame.mouse.set_visible(True)
    not_press = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens,bullets, scoreboard):
    screen_rect= screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            print("Gli alieni hanno raggiunto la base dello schermo!!!")
            ship_hit(ai_settings,stats,screen, aliens, ship, bullets, scoreboard)
            break

def update_aliens(ai_settings, stats, screen,aliens, ship,bullets, scoreboard):
    #controllo se la flotta ha raggiunto il limite dello schermo
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #controllo se qualche alieno colpisce la navicella
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,stats,screen,aliens,ship,bullets, scoreboard)
        print("Navetta colpita!!!")
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets, scoreboard)

    if ai_settings.aliens_alive != len(aliens):
        ai_settings.aliens_alive = len(aliens)
        print("alieni rimasti:" + str(len(aliens)))



def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y= ai_settings.screen_height - ship_height - (alien_height*4) + 50
    number_rows= int(available_space_y/(alien_height*2))
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
    alien.rect.y = alien.rect.y + 2* alien_height * row_number + 50
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens, ship):
    alien = Alien(screen,ai_settings)  # istanza della classe Alieno utile per avere info sulla larghezza della rect
    number_aliens_x = get_number_of_alines(ai_settings, alien.rect.width)
    number_rows= get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    ship.center_ship()

   # pygame.display.update()
    #creiamo gli alieni
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number, row_number)

#end-------------------------aliens---------------------------------------

#start-------------------------shooting and button------------------------
def fire_bullets(ai_settings,screen, ship, bullets, stats):
    if len(bullets) < ai_settings.bullet_allowed and ship.is_alive:
        new_bullet = Bullet(ai_settings, screen, ship)
        laser_sound = mixer.Sound("static/sounds/laser.wav")
        laser_sound.set_volume(0.1)
        laser_sound.play()
        bullets.add(new_bullet)


def check_keydown_events(event,ai_settings, screen, ship, bullets, stats, aliens, scoreboard):
    if ship.is_alive:
        if event.key == pygame.K_RIGHT:
            # muovi la nave a destra
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # muovi la nave a sinistra
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            # ferma il movimento  della nave a destra
            ship.moving_forward = True
        elif event.key == pygame.K_DOWN:
            # muovi la nave a sinistra
            ship.moving_back = True
        elif event.key == pygame.K_SPACE:
            fire_bullets(ai_settings,screen,ship,bullets, stats)


    if event.key == pygame.K_q:    #uscita dal gioco premendo 'q'
        sys.exit()
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(ai_settings, screen, stats, aliens, bullets, ship, scoreboard)



def check_keyup_events(event,ship):

    if event.key == pygame.K_RIGHT:
        # ferma il movimento  della nave a destra
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # muovi la nave a sinistra
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # ferma il movimento  della nave a destra
        ship.moving_forward = False
    elif event.key == pygame.K_DOWN:
        # muovi la nave a sinistra
        ship.moving_back = False
    elif event.key == pygame.K_RETURN:
        ship.do_rotation180 = True


def start_game(ai_settings, screen, stats, aliens,bullets, ship, scoreboard):
    # reset le proprieta' del gioco
    ai_settings.initillize_dynamic_settings()

    # nascondere il cursore del mouse quando si avvio il gioco
    pygame.mouse.set_visible(False)

    # distruzione oggetti a schermo non necessari e inizializzazione gioco
    stats.reset_stats()
    stats.game_active = True
    aliens.empty()
    bullets.empty()

    # reset scoreboard
    scoreboard.prep_high_score()
    scoreboard.prep_level()
    scoreboard.prep_score()
    scoreboard.prep_ships()

    # creazione
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()

def check_play_button(stats, play_button, x_mouse, y_mouse, ai_settings, screen, ship,aliens, bullets, scoreboard):
    button_clicked = play_button.rect.collidepoint(x_mouse, y_mouse)
    if button_clicked and  not stats.game_active:
        start_game(ai_settings, screen, stats, aliens, bullets, ship, scoreboard)



def check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens, scoreboard):
    # attendi un evento di input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT è un tipo di evento
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets, stats, aliens, scoreboard)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not ship.is_alive:
                ship.reset_flag()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button, mouse_x,mouse_y, ai_settings, screen, ship, aliens, bullets, scoreboard)


def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.write_high_score()
        scoreboard.prep_high_score()

def check_bullets_collisions(ai_settings, screen, ship, aliens,bullets, stats, scoreboard):
    # controllo se qualche proiettile ha colpito un alieno
    # in caso positivo, elimino entrambi gli oggetti (i due parametri passati di valore True)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        alien_hit_sound = mixer.Sound("static/sounds/alienHit.wav")
        alien_hit_sound.set_volume(0.5)
        alien_hit_sound.play()
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len (aliens)
            scoreboard.prep_score()
    if len(aliens)==0:
        #distruggiamo tutti i proiettili rimasti e creiamo una nuova flotta
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
        ai_settings.increase_speed()

        # aumento livello
        stats.level += 1
        scoreboard.prep_level()

# evitare leak memoria con oggetti fuori schermo
def update_bullets(ai_settings,screen, ship,bullets, aliens, stats, scoreboard):
    bullets.update()
    # cancellare i proiettili fuori dallo schermo
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= ai_settings.screen_height or not stats.game_active:
            bullets.remove(bullet)
    check_bullets_collisions(ai_settings,screen,ship,aliens,bullets, stats,scoreboard)

#end-------------------------shooting and button---------------------------

def update_screen(ai_settings, screen,stats, ship, aliens ,bullets, play_button, scoreboard):

    screen.fill( ai_settings.bg_color)  # per colorare lo sfondo
    #disegna tutti i proiettili dietro la nave e gli aleni
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #disegna gli alieni, si e' usato un modo diverso per fare la stessa cosa fatta per i proiettili nelle righe sopra
    aliens.draw(screen)
    ship.draw_me()
    scoreboard.draw_score()

    #creazione bottone se il gioco non è stato avviato
    if not stats.game_active:
        play_button.draw_button()

    # rendi lo schermo con gli oggetti più recenti visibile, aggiorna lo schermo
    pygame.display.update()
