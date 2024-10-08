import pygame.font

class Button():
    """ Essa classe representa um botão"""

    def __init__(self, ai_settings, screen, msg):
        # Inicializa os atributos do botão
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Definir as dimensões do botão
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Transforma msg em uma imagem renderizada e centraliza"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Desenha o botão"""

        # Desenha o botão em branco e, em seguida, desenha a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)