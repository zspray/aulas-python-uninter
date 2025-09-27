import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.ftfont import Font

from asset.DBproxy import DBproxy
from codes.Const import YELLOW, SCORE_POS, ORANGE, RED


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, game_mode:str, player_score:list[int]):
        pygame.mixer_music.load('asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBproxy('DBScore.db')
        name =  ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', YELLOW, SCORE_POS['Title'])
            if game_mode == 1:
                score = player_score[0]
                text = 'Enter Player 1 name (4 characters only):'
            if game_mode == 2:
                score = (player_score[0] + player_score[1]) /2
                text = 'Enter Team name (4 characters only):'
            if game_mode == 3:
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters only):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters only):'
            self.score_text(20, text, ORANGE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) <= 4:
                        db_proxy.save({'name':name, 'score':score, 'date': get_formatted_date()})
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, RED, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load('asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME           SCORE          DATE       ', ORANGE, SCORE_POS['Label'])
        db_proxy = DBproxy('DBScore.db')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        
        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect= text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass

def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%Y-%m-%d")
    return f"{current_date} {current_time}"