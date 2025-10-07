import pygame
from settings import COLORS

class Ememies():
    def __init__(self, x , y, tela):
        self.x = x
        self.y = y
        self.speed = 1
        self.tela = tela
        self.width = 40
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def update(self, player_pos):
        player_x, player_y = player_pos


        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed
        
        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed

        self.rect.topleft = (self.x, self.y)


    def criar_inimigo(self, tela):
        pygame.draw.rect(tela, COLORS['RED'], self.rect)
