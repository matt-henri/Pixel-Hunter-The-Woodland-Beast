from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.update_image('bullet.png')

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
        if self.rect.centerx > WIN_WIDTH:
            self.health = 0
