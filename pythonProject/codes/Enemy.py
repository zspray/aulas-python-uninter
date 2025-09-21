from codes.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 1

    def move(self,):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH