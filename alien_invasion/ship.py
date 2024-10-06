import pygame

class Ship():
    """ Essa classe representará a espaçonave"""

    def __init__(self, ai_settings, screen):
        """ Inicializa a espaçonave e define sua posição inicial"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load("images/rocket-1374247_1280.bmp")
        self.image = pygame.transform.scale(self.image, (80,120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        self.centerY = float(self.rect.bottom)

        # Movimenta a espaçonave
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """ Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.centerY -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.centerY

    def center_ship(self):
        """ Centraliza a espaçonave na tela"""

        self.center = self.screen_rect.centerx
        self.centerY = self.screen_rect.bottom
