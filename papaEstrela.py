import pygame,random
from nave import Nave
from estrela import Estrela
from sol import Sol

LARGURA = 500
ALTURA = 500
FPS = 200
terminou = False

# define colors
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.font.init()
pontos = 0
fonte = pygame.font.SysFont('Calibri', 30)
clock = pygame.time.Clock()  # controle do tempo para atualização da tela
fps = 100

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Papa estrelas")

estrelas = pygame.sprite.Group()  # estrelas
solParede = pygame.sprite.Group()

for i in range(60):
    x = random.randrange(LARGURA - 40)
    y = random.randrange(ALTURA - 20)
    estrela = Estrela(x, y)
    estrela.numero = i
    estrelas.add(estrela)

    for i in range(1):
        x = random.randrange(LARGURA - 40)
        y = random.randrange(ALTURA - 20)
        sol = Sol(x, y)
        sol.numero = i
        solParede.add(sol)

# grupo de personagens
listaSprites = pygame.sprite.Group()
nave = Nave(0, 100)
listaSprites.add(nave)
listaSprites.add(estrelas)
listaSprites.add(sol)


while terminou == False:
    # mantem o jogo rodando na velocidade correta
    clock.tick(fps)  # frequência de atualização
    nave.andar()
    filaEventos = pygame.event.get()
    for evento in filaEventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            nave.mudar_direcao(tecla)



            vetor = []
            vetor = pygame.sprite.spritecollide(nave, estrelas, True)

            for e in vetor:
                print(e.numero)

            pontos += len(vetor)


    # atualiza tela
    texto = fonte.render("Pontos: " + str(pontos), True, (VERMELHO))

    tela.fill(PRETO)
    tela.blit(texto, (0, 0))
    listaSprites.draw(tela)
    pygame.display.update()

pygame.quit()
