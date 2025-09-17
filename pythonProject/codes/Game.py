import pygame

from codes.Const import WIN_HEIGHT, WIN_WIDTH
from codes.Level import Level
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
            menu_return= menu.run(self.window)

            if menu_return in [1, 2, 3]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            else:
                pass
            pass

