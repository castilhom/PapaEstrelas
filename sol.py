import pygame

class Sol(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.image.load("sol.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 150])
        self.rect = self.image.get_rect()    # pega coordenadas
        self.direcao = 'direita'
        self.rect.x = x
        self.rect.y = y