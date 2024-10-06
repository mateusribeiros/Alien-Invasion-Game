import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    """ Inicializa o jogo e cria um objeto para a tela"""
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()


    # Cria aliens
    aliens = Group()

    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    # Inicia o laço principal do jogo
    while True:

        # Checa interações de mouse e teclado
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Atualiza as telas
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()