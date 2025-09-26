import pygame

from codes.Const import WIN_HEIGHT, WIN_WIDTH
from codes.Level import Level
from codes.Menu import Menu
from codes.Score import Score


class Game:
    def __init__(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH,WIN_HEIGHT))

    def run(self):
        print('Loop Start')
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return= menu.run(self.window)

            if menu_return in [1, 2, 3]:
                player_score = [0,0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save_score(menu_return, player_score)
            elif menu_return in [4]:
                score.show_score()
            else:
                pass
            pass

