import pygame

from codes.Menu import Menu


class Game:
    def __init__(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size = (600,480))

    def run(self):

        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Closh Window
                    quit() #end pygame
