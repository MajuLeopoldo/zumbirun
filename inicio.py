import pygame
import random
import math

# Inicialização do pygame
pygame.init()
pygame.display.set_caption("Zombie Run")

# Configurações da tela
larguraTela, alturaTela = 600, 700
tela = pygame.display.set_mode((larguraTela, alturaTela))  # tamanho da tela
clock = pygame.time.Clock()

# Player
hitBox = 40
andar = 4
correr = 6

# Cores
preto = (0, 0, 0)
roxo = (128, 0, 128)
verde = (0, 198, 34)
verdeEscuro = (0, 120, 10)
marrom = (141, 73, 37)
vermelho = (255, 0, 0)
branco = (255, 255, 255)


# Classe do Player
class Player:
    def __init__(self, x, y, velocidade):
        self.rect = pygame.Rect(x, y, hitBox, hitBox)
        self.velocidade = velocidade

    def atualizarPlayer(self):
        pygame.draw.rect(tela, preto, self.rect)

    def mover(self, dx, dy, trees):
        novo_x = self.rect.x + dx
        novo_y = self.rect.y + dy
        if pode_mover(novo_x, novo_y, trees):
            self.rect.x = novo_x
            self.rect.y = novo_y

# Classe da Árvore
class Tree:
    def __init__(self, x, y):
        self.rect_tronco = pygame.Rect(x, y, hitBox / 1.5, hitBox)
        self.rect_folhas = pygame.Rect(x - ((hitBox - hitBox / 1.5) / 2), y - hitBox * (2 / 3), hitBox, hitBox)

    def atualizarTree(self):
        pygame.draw.rect(tela, marrom, self.rect_tronco)
        pygame.draw.rect(tela, verdeEscuro, self.rect_folhas)

# Classe do Inimigo
class Enemy:
    def __init__(self, x, y, velocidade):
        self.rect = pygame.Rect(x, y, hitBox, hitBox)
        self.velocidade = velocidade

    def perseguir(self, player):
        xAlvo = player.rect.x - self.rect.x
        yAlvo = player.rect.y - self.rect.y
        distancia = math.sqrt(xAlvo**2 + yAlvo**2)

        if distancia != 0:
            xAlvo /= distancia
            yAlvo /= distancia
            self.rect.x += xAlvo * self.velocidade
            self.rect.y += yAlvo * self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, vermelho, self.rect)

# HUD
def desenharHUD():
    fonte = pygame.font.SysFont("Montserrat", 35)
    texto = fonte.render("Zombie Run", True, preto)
    tela.blit(texto, [larguraTela / 2 - texto.get_width() / 2, 10])

# Verifica colisão com árvores
def pode_mover(novo_x, novo_y, trees):
    rect_novo_player = pygame.Rect(novo_x, novo_y, hitBox, hitBox)
    for tree in trees:
        if rect_novo_player.colliderect(tree.rect_tronco):
            return False
    return True

# Tela de início
def tela_inicio():
    tela.fill(preto)
    fonte = pygame.font.SysFont("Montserrat", 50)
    texto = fonte.render("Zombie Run", True, verde)
    instrucoes = pygame.font.SysFont("Montserrat", 30).render("Pressione ENTER para jogar", True, branco)
    tela.blit(texto, (larguraTela / 2 - texto.get_width() / 2, alturaTela / 3))
    tela.blit(instrucoes, (larguraTela / 2 - instrucoes.get_width() / 2, alturaTela / 2))
    pygame.display.update()
    
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                esperando = False

# Função principal
def iniciarGame():
    tela_inicio()
    rodando = True
    player = Player(0, 0, andar)
    enemy = Enemy(50, 50, 2)
    trees = [Tree(random.randint(20, larguraTela - 20), random.randint(50, alturaTela - 25)) for _ in range(20)]

    while rodando:
        tela.fill(verde)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        keys = pygame.key.get_pressed()
        player.velocidade = correr if keys[pygame.K_LCTRL] else andar

        if keys[pygame.K_w]:
            player.mover(0, -player.velocidade, trees)
        if keys[pygame.K_s]:
            player.mover(0, player.velocidade, trees)
        if keys[pygame.K_d]:
            player.mover(player.velocidade, 0, trees)
        if keys[pygame.K_a]:
            player.mover(-player.velocidade, 0, trees)

        for tree in trees:
            tree.atualizarTree()

        enemy.perseguir(player)
        enemy.desenhar()
        player.atualizarPlayer()
        desenharHUD()
        pygame.display.update()
        clock.tick(24)

    pygame.quit()

iniciarGame()
