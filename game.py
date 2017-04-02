import pygame, sys
from pygame.locals import *
# GAME: INVASÃO ESPACIAL
#AUTOR: SISNANDO JUNIOR

largura = 900
altura = 400

class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('imagens/baladourada.png')

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria (self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar (self, superficie):
        superficie.blit(self.ImagemBala, self.rect)

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("imagens/nave.png")

        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 60

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

#CLASSE PARA DEFINIR O LIMITE DO MOVIMENTO DO JOGADOR
    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0

            elif self.rect.right > 900:
                self.rect.right = 900

    def disparar(self):
        print('Disparou')

    def colocar(self, superficie):
        superficie.blit(self.ImagemBala, self.rect)
    
#DEFININDO RESOLUÇÃO DA TELA E NOME DO JOGO
    def invasaoEspaco():
        pygame.init()
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Invasão do Espaço")

#ADICIONANDO IMAGEM DE FUNDO
        jogador = naveEspacial()
        ImagemFundo = pygame.image.load('imagens/fundo.jpg')
        jogando = True

    balaProjetil = Bala(largura / 2, altura - 60)

#COMANDOS DE MOVIMENTOS
    while True:
        jogador.movimento()
        balaProjetil.trajetoria()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jogador.rect.left -= jogador.velocidade

                    elif evento.key == K_RIGHT:
                        jogador.rect.right += jogador.velocidade

                    elif evento.key == K_SPACE:
                        jogador.disparar()

            tela.blit(ImagemFundo,(0,0))
            balaProjetil.colocar(tela)
            jogador.colocar(tela)
            pygame.display.update()

invasaoEspaco()


