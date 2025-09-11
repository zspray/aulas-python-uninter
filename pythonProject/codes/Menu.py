import pygame

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
            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end pygame

    def menu_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font = pygame.font.Font('Lucida Sans Typewriter', text_size)
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass