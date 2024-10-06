class Settings():
    """ Uma classe para armazenar todas as configurações da Invasão Alienígena"""

    def __init__(self):
        """ Inicializa as configurações do jogo"""

        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0,0,0)

        # Configurações da espaçonave
        self.ship_limit = 3

        # Configurações dos projéteis
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 255,255,0

        # Configurações dos alienígenas
        self.alien_width = 60
        self.alien_height = 60
        self.fleet_drop_speed = 10

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        self.bullet_scale = 2

        self.initialize_dynamic_settings()

        self.alien_points = 1

    def initialize_dynamic_settings(self):
        """ Inicializa as configurações que mudam no decorrer do jogo"""
        self.bullets_allowed = 3
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 0.8

    def increase_speed(self):
        """ Aumenta as configurações de velocidade"""
        self.bullets_allowed *= self.bullet_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
