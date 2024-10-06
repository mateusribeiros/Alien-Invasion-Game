import pygame
import random

from pygame.sprite import Sprite

class Alien(Sprite):
    """ Essa classe representará os aliens"""

    def __init__(self, ai_settings, screen):
        """ Inicializa o alien e define uma posição inicial"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alien e seu rect
        self.image = pygame.image.load(random.choice(["images/alien01.bmp", "images/alien02.bmp", "images/alien03.bmp"]))
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width,ai_settings.alien_height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada novo alien no centro da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)


    def update(self):
        """ Move o alienígena para a direita"""

        # Move o alienigena pra a esquerda ou pra direita
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Devolve True se o alienígena estiver na borda da tela"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True