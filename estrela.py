import pygame

class Estrela(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.image.load("estrela.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()    # pega coordenadas
        self.rect.x = x
        self.rect.y = y

    def andar(self):
        self.rect.x += 2

    def mudar_direcao(self, tecla):
        if tecla[pygame.K_UP]:
            self.rect.y += -5
        if tecla[pygame.K_DOWN]:
            self.rect.y += 5

    def sair(self, tecla):
         if tecla[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
