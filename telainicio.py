import sys

def tela_inicio():
    pygame.init()
    largura_tela, altura_tela = 600, 400
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Zombie Run - Início")
    
    # Carregar música
    pygame.mixer.music.load("musica_inicio.mp3")  # Certifique-se de ter esse arquivo na pasta
    pygame.mixer.music.play(-1)  # Loop infinito da música
    
    # Carregar fonte de zumbi
    fonte = pygame.font.Font("fonte_zumbi.ttf", 50)
    fonte_botao = pygame.font.Font("fonte_zumbi.ttf", 25)
    
    # Carregar imagens e redimensionar
    avatar = pygame.image.load("AvatarFront.png")
    zombie = pygame.image.load("Zumbi.Front.png")
    avatar = pygame.transform.scale(avatar, (70, 70))  # Aumenta o tamanho do avatar
    zombie = pygame.transform.scale(zombie, (70, 70))  # Aumenta o tamanho do zumbi
    
    cor_fundo = (34, 139, 34)  # Verde bonito como fundo
    cor_botao = (0, 200, 0)
    cor_botao_hover = (0, 255, 0)
    cor_texto = (255, 255, 255)
    
    botao_rect = pygame.Rect((largura_tela // 2 - 100, altura_tela // 2, 200, 50))
    
    rodando = True
    while rodando:
        tela.fill(cor_fundo)
        
        # Título
        titulo = fonte.render("PIBLOCK", True, cor_texto)
        tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, 100))
        
        # Botão Start
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if botao_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(tela, cor_botao_hover, botao_rect, border_radius=10)
        else:
            pygame.draw.rect(tela, cor_botao, botao_rect, border_radius=10)
        
        texto_botao = fonte_botao.render("START", True, cor_texto)
        texto_botao_rect = texto_botao.get_rect(center=botao_rect.center)
        tela.blit(texto_botao, texto_botao_rect.topleft)
        
        # Posicionar avatar e zumbi parados abaixo do botão
        avatar_x = largura_tela // 2 - 90
        avatar_y = altura_tela // 2 + 70
        zombie_x = largura_tela // 2 + 10
        zombie_y = altura_tela // 2 + 70
        
        tela.blit(avatar, (avatar_x, avatar_y))
        tela.blit(zombie, (zombie_x, zombie_y))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and botao_rect.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.stop()
                rodando = False  # Sai da tela de início e começa o jogo
        
        pygame.display.update()
    
    return  # Volta ao código principal para iniciar o jogo

# Chamar a tela de início antes de começar o jogo
tela_inicio()
