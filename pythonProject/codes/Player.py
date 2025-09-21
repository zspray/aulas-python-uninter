import pygame

from codes.Const import PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from codes.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 3

    def move(self,):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top>0:
            self.rect.move_ip(0, -self.speed)
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom<324:
            self.rect.move_ip(0, self.speed)
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left>0:
            self.rect.move_ip(-self.speed, 0)
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right<576:
            self.rect.move_ip(self.speed, 0)
        pass

