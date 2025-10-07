import pygame 
from settings import SCREEN_HEIGTH, SCREEN_WIDTH
from game import Game



def main():
    pygame.init()

    tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH), pygame.RESIZABLE)
    pygame.display.set_caption('Nome do jogo')

    game = Game(tela)

    game.run()

    pygame.quit()


if __name__ == "__main__" :
    main()