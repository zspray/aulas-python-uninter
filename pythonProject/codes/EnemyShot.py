from codes.Const import WIN_WIDTH
from codes.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 3

    def move(self,):
        self.rect.centerx -= self.speed
