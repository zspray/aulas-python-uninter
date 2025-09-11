import pygame

from codes.Const import WIN_HEIGHT, WIN_WIDTH
from codes.Menu import Menu


class Game:
    def __init__(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH,WIN_HEIGHT))

    def run(self):
        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run(self.window)
            pass

