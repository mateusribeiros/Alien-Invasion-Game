import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """ Responde a eventos de soltura de teclas e mouse"""

    # Observa eventos do teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y)

def check_keyup_events(event, ship):
    """ Responde a eventos de soltura de teclas"""

    # Observa eventos do teclado
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    """ Responde a eventos de pressionamento de teclas"""

    # Observa eventos do teclado
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        stats.game_active = False

def check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """ Inicia um novo jogo quando o botão Play é clicado"""

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()

        # Oculta o cursos do mouse
        pygame.mouse.set_visible(False)

        # Reinicia as informações do jogo
        stats.reset_stats()
        stats.game_active = True

        # Esvazia a lista de alienígenas e disparos
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ Atualiza as imagens na tela e alterna para a nova tela"""

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    # Desenha o botão play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigos"""
    # Atualiza as posições dos projéteis
    bullets.update()

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,bullets)

    # Livra-se de projéteis antigos
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Verifica as colisões entre os disparos e alienígenas """

    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()

    if len(aliens) == 0:
        # Destrói os projéteis existentes, cria uma nova frota e aumenta a velocidade do jogo
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullets(ai_settings, screen, ship, bullets):
    """ Dispara um novo projétil se o limite não foi alcançado"""

    # Cria um novo projétil e adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """ Cria uma frota completa de alienígenas"""

    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # O espaçamento entre os alienígenas é igual a largura de um alienígena

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria frota de alienígenas
    for row_number in range(number_rows):
        # Cria a primeira linha de alienígenas
        for alien_number in range(number_aliens_x):
            # Cria um alienígena e o posiciona na linha
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """ Determina o número de alienígenas que cabem em uma linha"""

    availabe_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(availabe_space_x / (2 * alien_width))

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Cria um alienigena e o posiciona na linha"""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determina o número de linhas com alienígenas que cabem na tela"""

    availabre_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(availabre_space_y / (2 * alien_height))

    return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """  Verifica se a frota está em uma das bordas
      e então atualiza as posições de todos os alienígenas da frota"""

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houver colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Verifica se algum alienígena atingiu a parte inferior
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """ Responde apropriadamente se algum alienígena alcançou a borda"""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ Faz toda a frota descer e muda sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Reage quando a espaçonave é atingida por alienígenas"""

    if stats.ships_left > 1:
        # Decrementa ships_left
        stats.ships_left -= 1

        # Esvazia a lista de alienígenas e projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Faz uma pausa
        sleep(0.5)

    else:
        stats.reset_stats()
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ Verifica se algum alien alcançou a parte inferior da tela"""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break