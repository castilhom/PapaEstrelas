import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.image.load("nave.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [92, 93])
        self.rect = self.image.get_rect()    # pega coordenadas
        self.direcao = 'direita'
        self.rect.x = x
        self.rect.y = y

    def andar(self):
        self.rect.x += 1

    def mudar_direcao(self, tecla):
        if tecla[pygame.K_UP]:
            self.rect.y += -2
        if tecla[pygame.K_DOWN]:
            self.rect.y += 2

    def sair(self, tecla):
         if tecla[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
