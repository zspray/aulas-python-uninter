import random

import pygame

from codes.Const import COLOR_BLUE, COLOR_ORANGE, WIN_HEIGHT, COLOR_YELLOW, EVENT_ENEMY
from codes.Enemy import Enemy
from codes.Entity import Entity
from codes.EntityFactory import EntityFactory
from codes.EntityMediator import EntityMediator
from codes.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name= name
        self.game_mode = game_mode # 1=1P, 2=2P COOP, 3=2P COMP
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        if self.game_mode in [2, 3]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f'asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player,Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice= random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',COLOR_YELLOW, (10, 5))
            self.level_text(14, f'fps:{clock.get_fps() : .0f}',COLOR_ORANGE, (WIN_HEIGHT - 20, 10))
            self.level_text(14, f'entidades:{len(self.entity_list)}',COLOR_YELLOW, (WIN_HEIGHT - 35, 10))


            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pass


    def level_text(self, text_size: int, text:str, text_color: tuple, text_pos:tuple):
        text_font = Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf = Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(top=text_pos[0], left=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)