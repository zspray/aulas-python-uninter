import pygame
from pygame import Rect, Surface

from codes.Const import WIN_WIDTH, BLUE, MENU_OPTION, ORANGE, YELLOW


class Menu:
    def __init__(self,window):
        self.window = window
        print('Menu Start')
        self.surf = pygame.image.load('asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left = 0,top = 0)

    def run(self,window):
        menu_option = 0
        pygame.mixer_music.load('asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Cloud", BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Forces", BLUE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], YELLOW, ((WIN_WIDTH / 2), (170 + i * 30)))
                else:
                    self.menu_text(30, MENU_OPTION[i], ORANGE, ((WIN_WIDTH / 2), (170 + i * 30)))

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option > len(MENU_OPTION) - 1:
                            menu_option = 0
                    if event.key == pygame.K_RETURN:
                        if menu_option == 0:
                            print('Start New Game 1P')
                            pygame.mixer_music.stop()
                            return 1
                        if menu_option == 1:
                            print('Start New Game 2P - COOPERATIVE')
                            pygame.mixer_music.stop()
                            return 2
                        if menu_option == 2:
                            print('Start New Game 2P - COMPETITIVE')
                            pygame.mixer_music.stop()
                            return 3
                        if menu_option == 3:
                            return 4 # Show Score
                            pass
                        if menu_option == 4:
                            print('Exit')
                            pygame.quit()

    def menu_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect= text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass