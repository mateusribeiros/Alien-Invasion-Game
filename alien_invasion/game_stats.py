from pygame.pypm import FALSE


class GameStats():
    """ Armazena dados estatísticos da Invasão Alienígena"""

    def __init__(self, ai_settings):
        """ Inicializa os dados estatísticos"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicializa o jogo em status inativo
        self.game_active = False

        self.ships_left = self.ai_settings.ship_limit

    def reset_stats(self):
        """ Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

