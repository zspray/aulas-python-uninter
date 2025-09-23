from codes.Const import WIN_WIDTH
from codes.EnemyShot import EnemyShot
from codes.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 1
        self.shot_delay = 100

    def move(self,):
        self.rect.centerx -= self.speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 100
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))