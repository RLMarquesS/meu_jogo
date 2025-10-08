import pygame
from settings import COLORS

class Player():
    def __init__(self, x , y, tela):
        self.x = x
        self.y = y
        self.speed = 10 
        self.tela = tela
        self.width = 40
        self.height = 50

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def move_player(self, comando):

        if comando[pygame.K_LEFT] or comando[pygame.K_a]:
            self.x -= self.speed
        if comando[pygame.K_RIGHT] or comando[pygame.K_d]:
            self.x += self.speed
        if comando[pygame.K_UP] or comando[pygame.K_w]:
            self.y -= self.speed
        if comando[pygame.K_DOWN] or comando[pygame.K_s]:
            self.y += self.speed
        
        self.rect.topleft = (self.x, self.y)

    def criar_player(self, tela):
        pygame.draw.rect(tela,COLORS['WHITE'], self.rect)

