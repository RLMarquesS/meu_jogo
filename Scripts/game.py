import pygame
from settings import FPS,COLORS,SCREEN_HEIGTH,SCREEN_WIDTH
from player import Player
from enemies import Ememies
from random import randint



class Game:
    #Construindo a classe Game
    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()
        self.running = True
        self.pontuacao = 0

        
        #Cria o player:
        self.player = Player(x=100, y=100, tela= self.tela)

        #Cria o inimigo:
        self.enemies = self.criar_inimigos(5)

    def run(self):
        #Função para deixar o jogo "rodando"
        while self.running:
            self.clock.tick(FPS)
            self.handless_events()
            self.update()
            self.fisica()
            self.player.criar_player(self.tela)
            for inimigo in self.enemies:
                inimigo.criar_inimigo(self.tela)

            self.mostrar_pontuacao(self.pontuacao, 36, COLORS['GREEN'],20,20)
            if not self.enemies:
                self.enemies = self.criar_inimigos(5)


            pygame.display.flip()


    def handless_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        comando = pygame.key.get_pressed()
        self.player.move_player(comando)



    def update(self):
        #Função de atualizarções do jogo
        pygame.display.update()
        
        #Atualiza a tela 
        self.tela.fill(COLORS['BLACK'])

        #Bloco INIMIGO 
            #criando inimigos:
        for inimigo in self.enemies:
            inimigo.update((self.player.x, self.player.y))
            #Verifica se há sobreposição de inimigos:
        self.evitar_sobreposicao_inimigos()



    def criar_inimigos(self, quantidade):
        inimigos = []
        for _ in range(quantidade):
            while True:
                x = randint(0,SCREEN_WIDTH - 40) #posisão na tela
                y = randint(0,SCREEN_HEIGTH - 50) #posisão na tela

                inimigo = Ememies(x, y, self.tela)
                

                if not any(inimigo.rect.colliderect(i.rect) for i in inimigos):
                    inimigos.append(inimigo)
                    break
        return inimigos
    
    def evitar_sobreposicao_inimigos(self):
        for i, inimigo in enumerate(self.enemies):
            for outro in self.enemies[i+1:]:
                inimigo.evitar_sobreposicao(outro)




    def fisica(self):
        for inimigo in self.enemies[:]:
            if self.player.rect.colliderect(inimigo.rect):
                self.pontuacao += 1
                self.enemies.remove(inimigo)

    

    def mostrar_pontuacao(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(None, tamanho)
        superficie_texto = fonte.render(f"Pontos : {texto}", True, cor)
        self.tela.blit(superficie_texto, (x, y))



