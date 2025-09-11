import pygame
from pygame import Rect, Surface

from codes.Const import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_ORANGE


class Menu:
    def __init__(self,window):
        self.window = window
        print('Menu Start')
        self.surf = pygame.image.load('asset/MenuBg.png')
        self.rect = self.surf.get_rect(left = 0,top = 0)

    def run(self,window):
        pygame.mixer_music.load('asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Cloud",COLOR_BLUE, ((WIN_WIDTH / 2),70))
            self.menu_text(50, "Forces", COLOR_BLUE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i],COLOR_ORANGE, ((WIN_WIDTH / 2),(170+i*30)))

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end pygame

    def menu_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect= text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass